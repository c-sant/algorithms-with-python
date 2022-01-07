import random
from typing import Callable, Tuple


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

        print(f"Sample: {array}")
        print(f"Sorted: {algorithm(array)}")

        return algorithm(array) == sorted(array)
    except:
        return False
