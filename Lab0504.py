'''Before Linked List'''

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

    def insert_before(self, node, data):
        '''insert before this node'''

        new_node = DataNode(data)

        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return

        if self.head.get_data() == node:
            new_node.set_next(self.head)
            self.head = new_node
            self.count += 1
            return

        current = self.head
        while current.get_next() is not None and current.get_next().get_data() != node:
            current = current.get_next()

        if current.get_next() is None:
            print("Cannot insert, " + node + " does not exist.")
            return

        new_node.set_next(current.get_next())
        current.set_next(new_node)

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

def main():

    '''main test'''

    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()


main()
