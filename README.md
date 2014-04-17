i3scripts
=========

create_worspace.py
==================

Propose to create a workspace according to the conf files.

select_child.py
===============
Allow to look for a child in the current workspace.

With this script, mark come handy, I personally use:

    bindsym $mod+m exec i3-input -P "Mark: " -F "mark %s"

show_scratchpad.py
==================

Like select_child.py but for scratchpad.

select_workspace.py
===================

Allow to focus or create and focus a new workspace.

Usage
=====

Can be used like this in the i3 config file:


    set $scripts ~/.i3/scripts/
    bindsym $mod+space exec --no-startup-id $scriptsselect_workspace.py
    bindsym $mod+Control+space exec --no-startup-id $scriptsselect_child.py
    bindsym $mod+Shift+w exec --no-startup-id $scriptscreate_workspace.py
    bindsym $mod+Shift+s exec --no-startup-id $scriptsshow_scratchpad.py
