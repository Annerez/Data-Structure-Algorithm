'''Personnel Information'''

class Person:

    '''Person's info'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):

        """Print person's detail"""

        return self.name + ", " + str(self.age) + " years old"

    def say_hello(self):

        """Say hello to this person!"""

        return "Hello, my name is " + self.name + "!"


def people(info):

    '''Get information'''

    print(info.get_details())
    print(info.say_hello())

people(Person(input(), int(input())))
