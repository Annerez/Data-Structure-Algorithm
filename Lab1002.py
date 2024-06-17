'''Labs 10.02 - ProbHash Hashing'''
class Student:
    '''Create 1 Student'''
    def __init__(self, sid=0, name="", gpa=0.0):
        '''Set Student [ID, Name, GPA]'''
        self.sid = int(sid)
        self.name = str(name)
        self.gpa = float(gpa)

    def get_sid(self):
        '''Get Student ID'''
        return int(self.sid)

    def get_name(self):
        '''Get Student Name'''
        return str(self.name)

    def get_gpa(self):
        '''Get Student GPA'''
        return float(self.gpa)

    def print_details(self):
        '''Print Student [ID, Name, GPA'''
        print("ID: %d\nName: %s\nGPA: %.02f" %(self.get_sid(), self.get_name(), self.get_gpa()))

class ProbHash:
    '''Create Hash Table'''
    def __init__(self, size):
        '''Set size and Hash Table'''
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash(self, key):
        '''return Index from key (ikey)'''
        while True:
            ikey = key % self.size
            if self.hash_table[ikey] == []:
                return int(ikey)
            else:
                return self.hash(self.rehash(key))

    def rehash(self, key):
        '''return key + 1 back to hash'''
        return int(key + 1) % self.size

    def insert_data(self, student):
        '''Insert given student data to Hash Table'''
        if [] in self.hash_table:
            ikey = self.hash(student.get_sid())
            self.hash_table[ikey] = student
            print("Insert %d at index %d" %(student.get_sid(), ikey))
        else:
            print("The list is full. %d could not be inserted." %(student.get_sid()))

    def search_data(self, sid):
        '''Find data from Student ID'''
        ikey = sid % self.size
        count = 0
        while self.hash_table[ikey] != [] and self.hash_table[ikey].get_sid() != sid\
        and count <= self.size:
            ikey = self.rehash(ikey)
            count += 1
        if self.hash_table[ikey] != [] and self.hash_table[ikey].get_sid() == sid:
            print("Found %d at index %d" % (sid, ikey))
            return self.hash_table[ikey]
        else:
            print("%d does not exist." % sid)
            return None

import json
def main():
    '''main code here'''
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
