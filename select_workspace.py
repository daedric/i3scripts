#!/usr/bin/env python

import i3
from utils.dmenu import dmenu

workspaces = i3.get_workspaces()
urgents = []
others = []

for workspace in workspaces:
  if workspace["urgent"]:
    urgents.append(workspace["name"])
  else:
    others.append(workspace["name"])

urgents.sort()
others.sort()

workspace = dmenu(urgents + others).strip()
i3.command("workspace", workspace)
