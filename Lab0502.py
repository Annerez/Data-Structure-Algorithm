'''Singly Linked List'''

class DataNode:

    '''Data Node'''

    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def get_data(self):

        '''get data from node'''

        return self.__data

    def set_data(self, data):

        '''set data in node'''

        self.__data = data

    def get_next(self):

        '''get next address from node'''

        return self.__next

    def set_next(self, new):

        '''set next address in node'''

        self.__next = new

class SinglyLinkedList:

    '''Linked List'''

    def __init__(self):
        self.count = 0
        self.head = None

    def insert_last(self, data):
        '''insert last index'''

        new_node = DataNode(data)
        self.count += 1

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()

            current.set_next(new_node)

    def traverse(self):
        '''traverse linkedlist'''

        current = self.head
        if self.head == None:
            print("This is an empty list.")
            return

        while current is not None:
            if current.get_next() == None:
                print(current.get_data())
            else:
                print(current.get_data(), end=" -> ")
            current = current.get_next()

LIST1_ = SinglyLinkedList()
for i in range(int(input())):
    LIST1_.insert_last(input())
LIST1_.traverse()
