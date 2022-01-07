def get_term(
        position: int,
        first_term: float,
        difference: float) -> float:
    """
    Returns the term at specified position in a given A.P.

    Parameters
    ------

    :param int position: the position of the term that needs to be returned.
    :param float first_term: the first term of the A.P.
    :param float difference: the common difference between the elements of the
    A.P.
    """
    return first_term + (position - 1) * difference


def get_sum(
        terms: int,
        first_term: float,
        difference: float) -> float:
    """
    Returns the sum of all of the values in a given A.P.

    :param int terms: the total number of terms the A.P has.
    :param float first_term: the first term of the A.P.
    :param float difference: the common difference between the elements of the
    A.P.
    """
    return (terms / 2) * (2 * first_term + (terms - 1) * difference)


if __name__ == '__main__':
    print(get_term(10, 1, 1))  # 10
    print(get_sum(10, 1, 1))  # sum of [1, 10] = 55
