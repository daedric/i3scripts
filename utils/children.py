import i3


def _format_nodes(nodes):
    return {
        node["id"]: {
            'name': node["name"],
            'mark': node.get("mark", ''),
            'raw': node,
        } for node in nodes}


def get_children(workspace):
    tree = i3.get_tree()
    workspace_info = i3.filter(tree, name=workspace["name"])
    nodes = i3.filter(workspace_info, nodes=[])
    return _format_nodes(nodes)


def get_scratchpad_children():
    container = i3.filter(name="__i3_scratch")[0]
    children = container["floating_nodes"]
    nodes = []
    for child in children:
        nodes += child.get("nodes", [])

    return _format_nodes(nodes)
