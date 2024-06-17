'''Summation'''

def summation_one(num):
    '''summtion'''

    total = 0
    for i in range(num + 1):
        total += i
    return total

def summation_two(num):
    '''summation formula'''
    return int(num * (num + 1) / 2)

def is_intersect(one, two, three):
    '''is it intersect?'''
    bool(set(one) & set(two) & set(three))

def calculator(num):
    '''calculator'''
    if num == 1:
        return 1
    total = 0
    for i in range(1, num + 1):
        total += (len(str(i))) + 1
    return total

def main():
    '''main function'''
    print(calculator(int(input())))

main()
