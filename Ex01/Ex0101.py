"""even"""

def odd_even(num):
    '''odd'''
    num = str(num)
    even = (2, 4, 6, 8, 0)
    if int(num[-1]) in even:
        print(True)
    else:
        print(False)

odd_even(int(input()))
