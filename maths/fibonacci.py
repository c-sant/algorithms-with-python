def fibonacci(n: int) -> int:
    """
    Returns a number in the specified position in the Fibonacci sequence.
    """
    if not (type(n) == int):
        raise TypeError("'n' should be an int")
    elif n < 0:
        raise ValueError("'n' should be positive")
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def get_sequence(n: int) -> list:
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
    """
    l = []

    for i in range(n + 1):
        l.append(fibonacci(i))

    return l


def is_fibonacci(n: int) -> bool:
    """
    Returns True if value is in Fibonacci sequence; otherwise, returns False.
    """

    i = 0
    fib = fibonacci(i)

    while fib <= n:
        if fib == n:
            return True

        i += 1

        fib = fibonacci(i)

    return False


if __name__ == '__main__':
    s = get_sequence(15)
    print(s)
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    print(s == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])
    # True

    print(is_fibonacci(610))  # True
    print(is_fibonacci(611))  # False
