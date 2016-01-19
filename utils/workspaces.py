import i3


def get_current_workspace():
    ws = i3.get_workspaces()
    for w in ws:
        if w["focused"]:
            return w
        else:
            raise Exception("can't find the focused workspace")
