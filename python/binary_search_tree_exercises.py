from typing import Optional

from binarytree import bst, Node

"""
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (float/int/str)
        self.left = left    # Left child
        self.right = right  # Right child
        """

def insert():
    pass
def min_from_tree(root:Node)->Optional[Node]:
    if root is None:
        return None

    node = root
    while node.left is not None:
        node = node.left
    return node

def max_from_tree(root:Node)->Optional[Node]:
    if root is None:
        return None
    node = root
    while node.right is not None:
        node = node.right
    return node

def get_predecessor(node:Node)->Optional[Node]:
    if node is None or node.left is None:
        return None
    return max_from_tree(node.left)

def get_successor(node:Node)->Optional[Node]:
    if node is None or node.left is None:
        return None
    return max_from_tree(node.left)

def lookup(root:Node, value)->tuple[Optional[Node], Optional[Node]]:
    #function returns both found node(tuple elem0) and its parent(tuple elem1)
    if root is None:
        return (None,None)
    if root.value == value:
        return (root, None)
    parent = root
    if parent.value > value:
        child = parent.left
    else:
        child = parent.right

    while child is not None and child.value != value:
        old_child = child
        if parent.value > value:
            child = parent.left
        else:
            child = parent.right
        parent = old_child

    return (child,parent)

def insert(root:Node, value):
    """function modifies tree"""
    child, parent = lookup(root, value)
    if child is not None:
        raise Exception("Not expecting this case, trying to insert a value which already exists in our bst")
    if parent is None:
        raise Exception("This is really unexpected")
    if value> parent.value:
        parent.right = Node(value)
    else:
        parent.left = Node(value)

def delete(root:Node, value):
    child, parent = lookup(root,value)
    if child is None:
        print("we could not find node with requested value, to delete")
    if child.left is None and child.right is None:
        if parent.left == child:
            parent.left = None
        else:
            parent.right = None
    elif child.left is not None and child.right is not None:
        predecessor = get_predecessor(child)
        delete(root,predecessor.value)
        child.value = predecessor.value

    elif child.left is None:
        if parent.left == child:
            parent.left = child.right
        else:
            parent.right = child.right
    else:
        if parent.left == child:
            parent.left = child.left
        else:
            parent.right = child.left



if __name__ == "__main__":
    my_bst = bst(height=3, is_perfect=False)
    print(my_bst)
    print(type(my_bst))
    print("min of this tree: ", min_from_tree(my_bst).value)
    print("")

    root = Node(1)  # index: 0, value: 1
    root.left = Node(0.5)  # index: 1, value: 2
    root.left.left = Node(-5)
    root.left.left.right = Node(0)
    root.right = Node(3)  # index: 2, value: 3
    root.right.right = Node(4)  # index: 4, value: 4
    root.right.right.right = Node(5)  # index: 9, value: 5
    print(root)
    print("looking for node with value 10: ",lookup(root,10))
    insert_val = -1
    insert(root,insert_val)
    print(f"after inserting value{insert_val}, this is how our tree looks like: {root}")
    insert_val = -10
    insert(root,insert_val)
    print(f"after inserting value{insert_val}, this is how our tree looks like: {root}")

    delete_val = 3
    delete(root,delete_val)
    print(f"after deleting value{delete_val}, this is how our tree looks like: {root}")

    delete_val = 1
    delete(root,delete_val)
    print(f"after deleting value{delete_val}, this is how our tree looks like: {root}")




