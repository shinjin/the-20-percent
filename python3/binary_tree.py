

def traverse_tree(root):
    if root:
        # preorder
        traverse_tree(root.left)
        print(f"Preorder: {root.data}")

        # inorder
        traverse_tree(root.right)
        print(f"Inorder: {root.data}")

        # postorder
        print(f"Postorder: {root.data}")



class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
