'''BST'''

class BSTNode:

    '''BST'''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    '''BST'''

    def __init__(self):
        self.root = None

    def get_root(self):
        '''getting root'''
        return self.root

    def set_root(self, root):
        '''setting root'''
        self.root = root

    def insert(self, data):
        '''insertion'''
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        '''insert recursion'''
        if data < current_node.data:
            if current_node.left:
                self._insert_recursive(current_node.left, data)
            else:
                current_node.left = BSTNode(data)
        elif data > current_node.data:
            if current_node.right:
                self._insert_recursive(current_node.right, data)
            else:
                current_node.right = BSTNode(data)

    def preorder(self):
        '''preorder'''
        if not self.root:
            print("Tree is empty.")
        else:
            self._preorder_recursive(self.root)
            print()

    def _preorder_recursive(self, current_node):
        '''preorder recursion'''
        if current_node:
            print(f"-> {current_node.data}", end=" ")
            self._preorder_recursive(current_node.left)
            self._preorder_recursive(current_node.right)

def main():
    '''Main'''
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
