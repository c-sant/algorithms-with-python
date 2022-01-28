from typing import Union


def selection_sort(
        array: list,
        inplace: bool = False) -> Union[list, None]:
    """
    A comparison sorting algorithm which sorts a given array by moving it's
    smallest values to the beggining one at a time.
    """

    if not inplace:
        array = array.copy()

    n = len(array)

    for i in range(n):
        smallest_value = array[i]
        smallest_index = i
        for j in range(i, n):
            if array[j] < smallest_value:
                smallest_value = array[j]
                smallest_index = j

        array[smallest_index], array[i] = array[i], array[smallest_index]

    if not inplace:
        return array