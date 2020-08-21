#!/usr/bin/python3

def bubbleSort(arr, reverse=False):
    length = len(arr)

    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    if reverse:
        arr.reverse()

    return arr