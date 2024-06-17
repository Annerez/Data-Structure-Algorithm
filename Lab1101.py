'''Insertion Sort'''

import json

def insertion(arr, last):
    '''insetion Sort'''

    current = 1
    hold = 0
    walker = 0
    count = 0
    for _ in range(last):
        hold = arr[current]
        walker = current - 1
        while walker >= 0 and hold < arr[walker]:
            arr[walker + 1] = arr[walker]
            walker -= 1
            count += 1
        if hold > arr[walker] and walker != -1:
            count += 1
        arr[walker + 1] = hold
        print(arr)
        current += 1
    print("Comparison times: " + str(count))

def main():
    '''main function'''

    arr = json.loads(input())
    last = int(input())
    insertion(arr, last)

main()

'''
        issort = True
        for j in range(last):
            if arr[j] > arr[j+1]:
                issort = False
                break
        if issort == True:
            break
        count += 1

'''
