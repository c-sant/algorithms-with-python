def linear_search(
        array: list,
        item: int) -> int:
    """
    A search algorithm that loops through a given array comparing each element
    to a given searched value. When the element and the value are the same, the
    index of the element is returned.

    If the value is not found in the array, it returns -1.
    """

    for index, value in enumerate(array):
        if item == value:
            return index

    return -1