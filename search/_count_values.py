from typing import Any


def count_element(array: list, element: Any) -> int:
    """
    Returns the amount of times a certain element occurs in a given array.
    """

    total = 0

    for i in array:
        if i == element:
            total += 1

    return total


def count_elements(array: list) -> dict:
    """
    Returns the amount of times each element appears in a given array.
    """

    d = {}

    if len(array) == 0:
        return d

    for element in array:
        if element not in d.keys():
            d[element] = 1
        else:
            d[element] += 1

    return d