from typing import Union, Callable

def wave_sort(
    array: list,
    inplace: bool = False,
    algorithm: Union[str, Callable] = 'default') -> Union[list, None]:
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