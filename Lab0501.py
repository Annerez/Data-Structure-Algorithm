'''Data Node'''

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


_PNEW = DataNode()
_PNEW.set_data(input())
print(_PNEW.get_data())
print(_PNEW.get_next())
