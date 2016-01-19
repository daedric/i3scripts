#!/usr/bin/env python

import os
import i3
import json
import sys
from utils.dmenu import dmenu
from utils.container import Container

current_dir = os.path.dirname(os.path.realpath(__file__))

workspaces_dir = os.path.join("~", ".i3", "workspaces")
workspaces_dir = os.path.expanduser(workspaces_dir)
workspaces = [file for file in os.listdir(workspaces_dir) if file.endswith(".conf")]
workspace = dmenu([os.path.splitext(w)[0] for w in workspaces])
workspace = workspace.strip() + ".conf"

workspace = os.path.join(workspaces_dir, workspace)
workspace = json.load(open(workspace))

existing_workspaces = i3.get_workspaces()

wname = workspace.get("name")

if wname:
    i3.workspace(wname)
    if wname in [w["name"] for w in existing_workspaces]:
        sys.exit(0)

root = workspace.get("root", "")
root = os.path.expanduser(root)

containers = []
for container in workspace["containers"]:
    c = Container(container)
    c.run(root)
    containers.append(c)

# here because we can modify the size only when we have all containers launched
for c in containers:
    c.apply_size()

# resize require focus
for c in containers:
    if c.focus:
        c.enable_focus()
        break
