from typing import Callable, Tuple
import random
from sorting import *

def test_sort(
        algorithm: Callable,
        sample_range: Tuple = (0, 250),
        sample_size: int = 10) -> bool:
    """
    Executes a sorting algorithm in a random sample to test if it is working
    correctly.

    Comparison is made with Python's "sorted" function implementation.
    """
    try:
        array = random.sample(range(*sample_range), sample_size)

        return algorithm(array) == sorted(array)
    except:
        return False

def test_wave_sort():
    t = list(range(1, 11))

    return wave_sort(t) == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

if __name__ == "__main__":
    print(
        f"Bubble Sort: {'OK' if test_sort(bubble_sort) else 'FAILED'}\n"
        f"Insertion Sort: {'OK' if test_sort(insertion_sort) else 'FAILED'}\n"
        f"Merge Sort: {'OK' if test_sort(merge_sort) else 'FAILED'}\n"
        f"Quick Sort: {'OK' if test_sort(quick_sort) else 'FAILED'}\n"
        f"Selection Sort: {'OK' if test_sort(selection_sort) else 'FAILED'}\n"
        f"Wave Sort: {'OK' if test_wave_sort() else 'FAILED'}"
    )