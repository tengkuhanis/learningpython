#bst can never have duplicated numbers
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key #to check if the  is value already there
            return root
        elif root.val < key #inserts at the right subtree
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
