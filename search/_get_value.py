def get_kth_smallest(array: list, k: int = 1):
    """
    Returns the kth smallest number in array.
    """

    if k <= 0 or k > len(array):
        raise IndexError("k is out of range")
    
    array = sorted(array)

    return array[k - 1]


def get_kth_largest(array: list, k: int = 1):
    """
    Returns the kth largest number in given array.
    """
    if k <= 0 or k > len(array):
        raise IndexError("k is out of range")

    array = sorted(array, reverse=True)

    return array[k - 1]

if __name__ == '__main__':
    from _test import test_get_value

    result = test_get_value(get_kth_smallest)
    
    print(result)

    result = test_get_value(get_kth_largest)

    print(result)