from typing import Union

def _partition(array: list, start: int, end: int) -> int:
    """
    Auxiliary function to get pivot index.
    """
    pivot = array[end]

    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[end] = array[end], array[i + 1]

    return i + 1

def quick_sort(
    array: list,
    start: int = 0,
    end: int = None,
    inplace: bool = False) -> Union[list, None]:
    """
    A "divide and conquer" algorithm based on picking an element as pivot and 
    dividing a given array based on it.
    """

    if not inplace:
        array = array.copy()

    if end == None:
        end = len(array) - 1

    if start < end:
        p = _partition(array, start, end)

        quick_sort(array, start, p - 1, True)
        quick_sort(array, p + 1, end, True)

    if not inplace:
        return array

if __name__ == "__main__":
    from _test import test_sort

    result = test_sort(quick_sort)
    
    print(result)