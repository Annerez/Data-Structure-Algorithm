'''Front Linked List'''

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

    def insert_front(self, data):
        '''insert front index'''

        new = DataNode(data)
        new.set_next(self.head)

        self.head = new
        self.count += 1

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
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    else:
        print("Invalid Condition!")
LIST1_.traverse()
