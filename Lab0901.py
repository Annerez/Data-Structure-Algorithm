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

def main():
    '''main function'''
    print(summation_two(int(input())))

main()
