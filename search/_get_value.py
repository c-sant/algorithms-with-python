from typing import Any


def get_kth_smallest(array: list, k: int = 1) -> Any:
    """
    Returns the kth smallest number in array.
    """

    if k <= 0 or k > len(array):
        raise IndexError("k is out of range")

    array = sorted(array)

    return array[k - 1]


def get_kth_largest(array: list, k: int = 1) -> Any:
    """
    Returns the kth largest number in given array.
    """
    if k <= 0 or k > len(array):
        raise IndexError("k is out of range")

    array = sorted(array, reverse=True)

    return array[k - 1]
