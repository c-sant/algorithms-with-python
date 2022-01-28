def binary_search(
        array: list,
        item: int) -> int:
    """
    A search algorithm that compares the target value to the middle element of
    the array.

    - if they are equal, the index is returned; 
    - if the middle element is larger than the target value, the search is 
    performed again using the middle element as the last element of the 
    interval; 
    - if the middle element is smaller than the value, the search is performed
    again using the middle element as the first element of the interval. 

    This proccess is repeated until the value is found.

    If the value is not found, it returns -1.
    """

    start = 0
    end = len(array) - 1

    while (end - start) >= 0:
        mid = (end + start) // 2

        if array[mid] == item:
            return mid

        elif array[mid] > item:
            end = mid

        else:
            start = mid + 1

    return -1


def recursive_binary_search(
        array: list,
        item: int,
        start: int = 0,
        end: int = None) -> int:
    """
    A recursive version of the Binary Search algorithm.
    """

    if end == None:
        end = len(array) - 1

    if (end - start) < 0:
        return -1

    mid = (end + start) // 2

    if array[mid] == item:
        return mid

    elif array[mid] > item:
        return recursive_binary_search(array, item, start, mid)

    else:
        return recursive_binary_search(array, item, mid + 1, end)