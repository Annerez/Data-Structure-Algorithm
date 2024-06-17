'''Selection Sort'''

import json

def selection(arr, last):
    '''insetion Sort'''

    current = 0
    smallest = 0
    walker = 0
    count = 0
    temp = 0
    flag = False
    flagval = 0
    for _ in range(last):
        smallest = arr[current]
        walker = current + 1
        while walker <= last:
            if arr[walker] < smallest:
                smallest = arr[walker]
                flag = True
                flagval = walker
            count += 1
            walker += 1
        if flag == True:
            temp = arr[current]
            arr[current] = smallest
            arr[flagval] = temp
        print(arr)
        current += 1
        flag = False
    print("Comparison times: " + str(count))

def main():
    '''main function'''

    arr = json.loads(input())
    last = int(input())
    selection(arr, last)

main()

