def recursive_factorial(n: int) -> int:
    """
    Returns n! value using recursive method.
    """
    if not (type(n) == int):
        raise TypeError("'n' should be an int")
    elif n < 0:
        raise ValueError("'n' should be positive")
    elif n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


def iterative_factorial(n: int) -> int:
    """
    Returns n! value using iterative method.
    """
    if not (type(n) == int):
        raise TypeError("'n' should be an int")
    elif n < 0:
        raise ValueError("'n' should be positive")
    elif n <= 1:
        return 1
    else:
        total = 1
        for i in range(1, n + 1):
            total *= i

        return total


if __name__ == "__main__":
    print(recursive_factorial(5))  # 120
    print(iterative_factorial(5))  # 120
