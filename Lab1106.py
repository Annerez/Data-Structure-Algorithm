'''Bubble Sort'''

import json

def bubble(arr, last):
    '''Bubble Sort'''

    key = 0
    status = False
    time = 0
    while key <= last and status is False:
        walker = last
        status = True
        while walker > key:
            if ord((arr[walker])[0]) == ord((arr[walker - 1])[0]):
                if int((arr[walker])[1:]) < int((arr[walker - 1])[1:]):
                    status = False
                    arr[walker], arr[walker - 1] = arr[walker - 1], arr[walker]
            elif ord((arr[walker])[0]) < ord((arr[walker - 1])[0]):
                status = False
                arr[walker], arr[walker - 1] = arr[walker - 1], arr[walker]
            time += 1
            walker -= 1
        print(arr)
        key += 1
    print("Comparison times:", time)


def main():
    '''main'''

    arr = json.loads(input())
    last = int(input())
    bubble(arr, last)

main()
