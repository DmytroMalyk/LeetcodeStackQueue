class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    res = []
    res.append(node.data)
    res += pre_order(node.left)
    res += pre_order(node.right)
    return res

# In-order traversal
def in_order(node):
    if node is None:
        return []
    res = []
    res += in_order(node.left)
    res.append(node.data)
    res += in_order(node.right)
    return res

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    res = []
    res += post_order(node.left)
    res += post_order(node.right)
    res.append(node.data)
    return res
