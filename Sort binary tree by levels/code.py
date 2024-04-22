def tree_by_levels(node):
    def height_dict(node, height, dict):
        if not node:
            return
        if height in dict:
            dict[height].append(node.value)
        else:
            dict[height] = [node.value]
        height_dict(node.left, height+1, dict)
        height_dict(node.right, height+1, dict)
    height_dict(node, 0, ( res := {} ))
    return [el for key in res for el in res[key]]
