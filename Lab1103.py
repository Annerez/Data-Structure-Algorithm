'''Bubble Sort'''

import json

def bubble(arr, last):
    '''Bubble sort'''

    current = 0
    issort = False
    walker = 0
    count = 0
    while current <= last and issort == False:
        walker = last
        issort = True
        while walker > current:
            if arr[walker] < arr[walker - 1]:
                issort = False
                temp = arr[walker]
                arr[walker] = arr[walker - 1]
                arr[walker - 1] = temp
            count += 1
            walker -= 1
        print(arr)
        current += 1
    print("Comparison times: %d" %count)

def main():
    '''main function'''

    arr = json.loads(input())
    last = int(input())
    bubble(arr, last)

main()

