'''Elevator'''

class Elevator:

    '''Elevator'''

    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor_number):

        '''change floor'''
        if floor_number <= self.max_floor:
            self.current_floor = floor_number
        else:
            print("Invalid Floor!")

    def report_current_floor(self):

        '''tell current floor'''

        return self.current_floor

def elevator():

    '''elevator'''

    ele = Elevator(int(input()))
    floor = input()
    while floor != "Done":
        floor = int(floor)
        ele.go_to_floor(floor)
        floor = input()
    print(ele.report_current_floor())

elevator()
