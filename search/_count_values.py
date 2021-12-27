def count_element(array: list, element):
    """
    Returns the amount of times a certain element occurs in a given array.
    """

    if (element not in array) or len(array) == 0:
        return 0
    
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

if __name__ == '__main__':
    array = [2, 1, 5, 11, 20, 2, 6, 11, 6, 7, 2, 5]
    print(count_elements(array))
    print(count_element(array, 2))


    # works with string too
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    print(count_elements(text))

