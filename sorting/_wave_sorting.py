from typing import Union, Callable

def wave_sort(
    array: list,
    inplace: bool = False,
    algorithm: Union[str, Callable]= 'default'):
    """
    Returns array sorted in a wave form.

    Wave form:
    array[0] >= array[1] <= array[2] >= array[3] <= array[4]
    """

    if not inplace:
        array = array.copy()

    if algorithm == 'default':
        array = sorted(array)
    else:
        array = algorithm(array)
    
    for i in range(0, len(array) - 1, 2):
        array[i], array[i + 1] = array[i + 1], array[i]

    if not inplace:
        return array

if __name__ == '__main__':
    sample = [8, 1, 3, 5, 7, 4, 10, 9, 6, 2]
    print(wave_sort(sample))
    # sorted sample: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # wave sample: [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
