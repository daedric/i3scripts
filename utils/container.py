import re
import i3
from . import workspaces, children
from i3exec import i3exec


class Container:
    def __init__(self, d):
        self.name = d.get("name")
        self.command = d.get("command")
        self.run_in_term = d.get("run_in_term")
        self.focus = d.get("focus")
        self.title = d.get("title")
        self.delay = d.get("delay", 0.1)
        self.split = d.get("split")
        self.layout = d.get("layout")
        self.width = d.get("width")
        self.height = d.get("height")

    def run(self, root=None):
        if self.command:
            command = self.command.format(container=self)
            i3exec(command, root=root, sleep=self.delay)
        elif self.run_in_term:
            self.run_in_term = self.run_in_term.format(container=self)
            command = 'i3-sensible-terminal -title {container.title} -e ${{SHELL}} -i -c "{container.run_in_term}"'.format(container=self)
            i3exec(command, root=root, sleep=self.delay)
        else:
            raise Exception("no command")
        self.layout and i3.layout(self.layout)
        self.split and i3.split(self.split)

    def get_current_i3_container(self):
        if not self.title:
            raise Exception("title required")
        w = workspaces.get_current_workspace()

        title = re.compile(self.title)
        for id, child in children.get_children(w).iteritems():
            if title.match(child["name"]):
                return (id, child)

    def _resize(self, pct, orientation):
        self.enable_focus()
        w = workspaces.get_current_workspace()
        w_orientation_size = w["rect"][orientation]
        expected_orientation_size = pct * w_orientation_size

        id, child = self.get_current_i3_container()
        child = child["raw"]
        c_orientation_size = child["rect"][orientation]

        px = expected_orientation_size - c_orientation_size
        action = "grow"

        if px < 0:
            px = -px
            action = "shrink"

        ppt = int(100 * (px / w_orientation_size))

        px = int(px)
        i3.command("resize", action, orientation,
                   "{}".format(px),
                   "px",
                   "or",
                   "{}".format(ppt),
                   "ppt")

    def apply_size(self):
        self.width and self._resize(self.width, "width")
        self.height and self._resize(self.height, "height")

    def enable_focus(self):
        id, child = self.get_current_i3_container()
        i3.focus(con_id=id)
