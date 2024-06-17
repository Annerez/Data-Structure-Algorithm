'''Stack'''

class ArrayStack:

    '''Stack & Queue'''

    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):

        """stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):

        """delete data"""
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()

    def is_empty(self):

        """check if empty"""
        return True if self.data == [] else False

    def get_stack_top(self):

        """return top stack value"""
        if self.data == []:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]

    def get_size(self):

        """tell size"""

        return self.size

    def print_stack(self):

        """print data in stack"""

        print(self.data)

def is_parentheses_matching(expr):

    '''check parent'''

    stack = ArrayStack()
    check = True

    parentheses_mapping = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                check = False
            top_element = stack.pop()
            if parentheses_mapping[char] != top_element:
                check = False

    if not stack.is_empty():
        return False

    return check

EXPR_ = input()
RES_ = is_parentheses_matching(EXPR_)

print(RES_)

