"""Rectangle Class"""

class Rectangle:

    '''Rectangle classes'''

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):

        '''calculate rectangle area'''

        return self.height * self.width

    def calculate_perimeter(self):

        '''calculate rectangle perimeter'''

        return (self.height * 2) + (self.width * 2)


def rec():

    '''Get detail'''

    rec = Rectangle(float(input()), float(input()))
    con = input()
    if con == 'area':
        result = rec.calculate_area()
    else:
        result = rec.calculate_perimeter()
    print('%.2f' % result)

rec()
