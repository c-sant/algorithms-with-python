def get_term(
        position: int,
        first_term: float,
        ratio: float) -> float:
    """
    Returns the term at specified position in a given G.P.

    Parameters
    ------

    :param int position: the position of the term that needs to be returned.
    :param float first_term: the first term of the G.P.
    :param float ratio: the common ratio between the elements of the
    G.P.
    """
    return first_term * ratio ** (position - 1)


def get_sum(
        terms: int,
        first_term: float,
        ratio: float) -> float:
    """
    Returns the sum of all of the values in a given G.P.

    :param int terms: the total number of terms the G.P has.
    :param float first_term: the first term of the G.P.
    :param float ratio: the common ratio between the elements of the
    G.P.
    """
    return (first_term * abs(ratio ** terms - 1)) / abs(ratio - 1)