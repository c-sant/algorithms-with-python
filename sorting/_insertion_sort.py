def insertion_sort(
    array: list, 
    inplace: bool = False) -> list:
    """
    A sorting algorithm that organizes values in an array one at a time. It 
    loops through the inserted array until it finds a value in a wrong 
    position. Then, it shifts the value's position until it fits. The process 
    is repeated until every value is in it's place.
    """

    if not inplace:
        array = array.copy()

    n = len(array)

    for j in range(1, n):
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1

    if not inplace:
        return array

if __name__ == "__main__":
    from _test import test_sort

    result = test_sort(insertion_sort)

    print(result)