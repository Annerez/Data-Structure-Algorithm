'''classify name'''

def heapify(arr, num, i):

    '''Heap sort algo'''

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < num and arr[i] < arr[left]:
        largest = left

    if right < num and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, num, largest)

def heap(arr):

    '''heap'''

    num = len(arr)

    for i in range(num, -1, -1):
        heapify(arr, num, i)

    for i in range(num - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def classify(number):

    '''by alphabet'''

    arr = []
    for _ in range(number):
        name = input()
        arr.append(name)
    heap(arr)
    for i in arr:
        print(i)

classify(int(input()))
