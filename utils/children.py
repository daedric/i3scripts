import i3

def get_children(workspace):
  tree = i3.get_tree()
  workspace_info = i3.filter(tree, name=workspace["name"])
  nodes = i3.filter(workspace_info, nodes=[])

  return {
      node["id"]: {
        'name': node["name"],
        'mark': node.get("mark", ''),
        'raw': node,
        } for node in  nodes}
