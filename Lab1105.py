'''Selection Sort'''

import json

def selection(arr, last):
    '''Selection Sort'''

    time = 0
    key = 0
    while True:
        if key == last:
            break
        sss = key
        www = key + 1
        while True:
            if www > last:
                break
            word_w = arr[www]
            word_s = arr[sss]
            if ord(word_w[0]) == ord(word_s[0]):
                if int(word_w[1:]) < int(word_s[1:]):
                    sss = www
            elif ord(word_w[0]) < ord(word_s[0]):
                sss = www

            www += 1
            time += 1
        arr[key], arr[sss] = arr[sss], arr[key]
        print(arr)
        key += 1
    print("Comparison times:", time)

def main():
    '''main'''

    arr = json.loads(input())
    last = int(input())
    selection(arr, last)

main()
