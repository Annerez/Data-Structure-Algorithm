'''BST'''

class BSTNode:

    '''BST'''

    def __init__(self, data) -> None:
        self.data = int(data)
        self.left = None
        self.right = None

    def set_data(self, data):
        '''setting data'''
        self.data = int(data)

    def set_left(self, left_node):
        '''setting left'''
        self.left = left_node

    def set_right(self, right_node):
        '''setting right'''
        self.right = right_node

    def get_data(self):
        '''getting dta'''
        return self.data

    def get_left(self):
        '''getting left'''
        return self.left

    def get_right(self):
        '''getting right'''
        return self.right

class BST:

    '''BST'''

    def __init__(self) -> None:
        self.root = None

    def get_root(self):
        '''getting root'''
        return self.root

    def set_root(self, root):
        '''setting root'''
        self.root = root

    def insert(self, data):
        '''insertion'''
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        '''insertion'''
        if root is None:
            return BSTNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def preorder(self):
        '''preorder'''
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        '''pre order'''
        if root:
            print("->", root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def is_empty(self):
        '''is empty'''
        return self.root is None

    def inorder(self):
        '''in order'''
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        '''in order'''
        if root:
            self._inorder(root.left)
            print("->", root.data, end=" ")

            self._inorder(root.right)

    def postorder(self):
        '''post order'''
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        '''post order'''
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self):
        '''traverse'''
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('Inorder: ', end='')
        self.inorder()
        print('Postorder: ', end='')
        self.postorder()

    def _find_min(self, root):
        '''find min'''
        if self.is_empty():
            return None
        cur = root
        while cur.left:
            cur = cur.left
        return cur.data

    def find_min(self):
        '''find min'''
        return self._find_min(self.root)

    def find_max(self):
        '''find max'''
        return self._find_max(self.root)

    def _find_max(self, root):
        '''find max'''
        if self.is_empty():
            return None
        cur = root
        while cur.right:
            cur = cur.right
        return cur.data

def main():
    '''main code'''
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
