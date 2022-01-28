def recursive(n: int) -> int:
    """
    Returns a number in the specified position in the Fibonacci sequence
    using recursion.
    """
    if not (type(n) == int):
        raise TypeError("'n' should be an int")
    elif n < 0:
        raise ValueError("'n' should be positive")
    elif n <= 1:
        return n
    else:
        return recursive(n - 1) + recursive(n - 2)

def iterative(n: int) -> int:
    """
    Returns a number in the specified position in the Fibonacci sequence
    using iterations.
    """
    if not (type(n) == int):
        raise TypeError("'n' should be an int")
    elif n < 0:
        raise ValueError("'n' should be positive")
    elif n <= 1:
        return n
    else:
        x, y = 0, 1

        for i in range(n):
            x, y = y, x + y

        return x


def get_sequence(n: int, method: str = 'r') -> list:
    """
    Returns the Fibonacci sequence until the nth value, a series of numbers in
    which every number is composed by the sum of it's two preceding values.

    Example:

    - F0 = 0
    - F1 = 1
    - F2 = F1 + F0 = 1
    - F3 = F2 + F1 = 2
    - F4 = F3 + F2 = 3
    - F5 = F4 + F3 = 5
    ...  

    Has two methods: 'r' stands for recursive, while 'i' stands for iterative.
    """
    if n < 0:
        raise ValueError("'n' must be positive")

    method = method.strip().lower()

    if method not in ['r', 'i']:
        raise ValueError("'method' must be either 'r' or 'i'")

    if n <= 1:
        return [0, 1]

    l = []

    if method == 'r':
        for i in range(n + 1):
            l.append(recursive(i))
    
    elif method == 'i':
        x, y = 0, 1
        
        for i in range(n + 1):
            l.append(x)
            x, y = y, x + y            

    return l


def is_fibonacci(n: int, method: str = 'r') -> bool:
    """
    Returns True if value is in Fibonacci sequence; otherwise, returns False.

    Method can be either recursive ('r') or iterative ('i').
    """
    if n < 0:
        return False

    elif n <= 1:
        return True

    method = method.strip().lower()

    if method not in ['r', 'i']:
        raise ValueError("'method' must be either 'r' or 'i'")

    i = 0
    fib = recursive(i)

    while fib <= n:
        if fib == n:
            return True

        i += 1

        if method == 'r':
            fib = recursive(i) 
        elif method == 'i':
            fib = iterative(i)

    return False