'''BST'''

class BSTNode:

    '''BST'''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        '''getting data'''
        return self.data

    def set_data(self, new_data):
        '''setting data'''
        self.data = new_data

    def get_left(self):
        '''getting left data'''
        return self.left

    def set_left(self, new_left):
        '''setting left data'''
        self.left = new_left

    def get_right(self):
        '''getting right data'''
        return self.right

    def set_right(self, new_right):
        '''setting right data'''
        self.right = new_right

DATA_INPUT = int(input())
NODE = BSTNode(DATA_INPUT)
print(NODE.get_data())
print(NODE.get_left())
print(NODE.get_right())
