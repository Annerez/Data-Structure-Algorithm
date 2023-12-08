'''Find point'''

class Point:

    '''2 dimension'''

    def __init__(self, var_x=0, var_y=0):
        self.set_coordinates(var_x, var_y)

    def set_coordinates(self, var_x, var_y):
        '''set coordinate'''
        self.var_x = var_x
        self.var_y = var_y

    def get_coordinates(self):
        '''calculate coordinate'''
        return (self.var_x, self.var_y)

    def calculate_distance(self, other_point):
        '''calculate distance'''
        return ((other_point.var_x - self.var_x)**2 + (other_point.var_y - self.var_y)**2) ** 0.5

def distance():

    '''find distance'''
    boss = Point(float(input()), float(input()))
    art = Point(float(input()), float(input()))
    ans = ("%.2f" % art.calculate_distance(boss))
    print(ans)

distance()
