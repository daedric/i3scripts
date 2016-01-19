#!/usr/bin/env python

import i3
from utils import workspaces, dmenu
from utils.children import get_scratchpad_children
from pprint import pprint

reverse_dict = {}
l = []

i = 0
for id, child in get_scratchpad_children().iteritems():
    name, mark = child["name"], child["mark"]
    if mark:
        str = "{} - {} - {}".format(i, name, mark)
    else:
        str = "{} - {}".format(i, name)
        i = i + 1

    l.append(str)
    reverse_dict[str] = id

str = dmenu.dmenu(l).strip()
id = reverse_dict[str]

i3.focus(con_id=id)

