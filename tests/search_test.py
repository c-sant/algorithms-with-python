from search import *
import random
from typing import Callable, Tuple


def test_search(
        algorithm: Callable,
        sample_range: Tuple[int, int] = (0, 250),
        sample_size: int = 10) -> bool:
    """
    Executes a search algorithm in a random sample to test if it is working
    correctly.

    The algorithm must be able to find every single element of the array.
    """
    try:
        array = sorted(random.sample(range(*sample_range), sample_size))

        for index, value in enumerate(array):
            found_index = algorithm(array, value)

            if found_index != index:
                return False

        return True

    except:
        return False


def test_get_value(
        algorithm: Callable,
        sample_range: Tuple[int, int] = (0, 250),
        sample_size: int = 10) -> bool:
    try:
        array = random.sample(range(*sample_range), sample_size)
        test_array = []

        for i in range(1, len(array) + 1):
            test_array.append(algorithm(array, i))

        return (
            test_array == sorted(array) or
            list(reversed(test_array)) == sorted(array)
        )
    except:
        return False


def test_count_element():
    t = [1, 4, 7, 7, 7, 9, 13]

    return count_element(t, 7) == 3


def test_count_elements():
    t = "This is a test!"
    t_dict = {'T': 1, 'h': 1, 'i': 2, 's': 3,
              ' ': 3, 'a': 1, 't': 2, 'e': 1, '!': 1}

    return count_elements(t) == t_dict


if __name__ == '__main__':
    print(
        f"Binary Search (Recursive): {'OK' if test_search(recursive_binary_search) else 'FAILED'}\n"
        f"Binary Search (Iterative): {'OK' if test_search(binary_search) else 'FAILED'}\n"
        f"Linear Search: {'OK' if test_search(linear_search) else 'FAILED'}\n"
        f"Count Element in Array: {'OK' if test_count_element() else 'FAILED'}\n"
        f"List element occourences in Array: {'OK' if test_count_elements() else 'FAILED'}\n"
        f"Get kth smallest element in Array: {'OK' if test_get_value(get_kth_smallest) else 'FAILED'}\n"
        f"Get kth largest element in Array: {'OK' if test_get_value(get_kth_largest) else 'FAILED'}"
    )
