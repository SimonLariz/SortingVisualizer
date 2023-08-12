"""Implementations of various sorting algorithms"""


def bubble_sort(arr):
    """Bubble sort implementation, yields intermediate states of the array"""
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr
    yield arr


def selection_sort(arr):
    """Selection sort implementation, yields intermediate states of the array"""
    arr_len = len(arr)
    for i in range(arr_len):
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr
    yield arr
