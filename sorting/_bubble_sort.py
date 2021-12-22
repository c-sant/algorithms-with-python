def bubble_sort(
    array: list, 
    inplace: bool = False):
    """
    A sorting algorithm that loops through an unsorted array, comparing each 
    element with it's adjacent and swaping them if they are in the wrong order.
    This process is repeated until the array is completely sorted.
    """

    if not inplace:
        array = array.copy()

    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break
    if not inplace:
        return array

if __name__ == "__main__":
    from _test import test_sort

    result = test_sort(bubble_sort)

    print(result)