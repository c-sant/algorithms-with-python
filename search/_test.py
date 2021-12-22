import random
from typing import Callable, Tuple

def test_search(
    algorithm: Callable,
    sample_range: Tuple = (0, 250),
    sample_size: int = 10) -> bool:
    """
    Executes a search algorithm in a random sample to test if it is working
    correctly.

    The algorithm must be able to find every single element of the array.
    """
    try:
        array = sorted(random.sample(range(*sample_range), sample_size))

        for index, value in enumerate(array):
            found_index = algorithm(array, value)
            
            if found_index != index:
                return False
            
        return True

    except:
        return False
    
