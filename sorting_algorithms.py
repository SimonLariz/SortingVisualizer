"""Implementations of various sorting algorithms"""


def bubble_sort(arr):
    """Bubble sort implementation"""
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
