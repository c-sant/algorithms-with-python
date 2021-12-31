from typing import Union

def _merge(
    array: list, 
    start: int, 
    mid: int, 
    end: int) -> None:
    """
    Auxiliary function to merge and sort two arrays.
    """
    temp = []

    i, j = start, mid + 1

    while (i <= mid) and (j <= end):
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1
    
    while j <= end:
        temp.append(array[j])
        j += 1

    for k in range(len(temp)):
        array[start + k] = temp[k]

def merge_sort(
    array: list,
    start: int = 0,
    end: int = None,
    inplace: bool = False) -> Union[list, None]:
    """
    A "divide and conquer" sorting algorithm that divides the input array into
    two and applies itself in each of them to sort them before merging them 
    together afterwards.
    """

    if not inplace:
        array = array.copy()

    if end == None:
        end = len(array) - 1

    if start < end:
        mid = int((start + end) / 2)
        merge_sort(array, start, mid, True)
        merge_sort(array, mid + 1, end, True)

        _merge(array, start, mid, end)

    if not inplace:
        return array

if __name__ == "__main__":
    from _test import test_sort

    result = test_sort(merge_sort)

    print(result)