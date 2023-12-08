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

class Project:

    '''Project's information'''

    def __init__(self, project, member):
        self.project = project
        self.member = member

    def show_name(self):

        """Show Project's Name"""

        print("Hello There! This is " + self.project)
        return "This project has " + str(self.member) + " members"

    def show_mem(self):

        """Show Project's Members"""

        members = []
        for _ in range(self.member):
            someone = Person(input(), int(input()))
            members.append(someone.say_hello())

        return members

def people(proj):

    '''Get information'''
    mem = proj.show_mem()
    mem = sorted(mem)
    print(proj.show_name())
    print(*mem, sep="\n")

people(Project(input(), int(input())))
