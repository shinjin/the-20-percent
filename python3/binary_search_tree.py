

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



class BST:
    def __init__(self, root=None):
        self.root = root


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(self.root, data)


    def __insert(self, root, data):
        if data < root.data:
            if root.left:
                self.__insert(root.left, data)
            else:
                root.left = Node(data)
        else:
            if root.right:
                self.__insert(root.right, data)
            else:
                root.right = Node(data)


    def find(self, data):
        if self.root:
            return self.__find(self.root, data)
        else:
            return None


    def __find(self, root, data):
        if root.data == data:
            return root

        if data < root.data:
            return self.__find(root.left, data)
        else:
            return self.__find(root.right, data)

