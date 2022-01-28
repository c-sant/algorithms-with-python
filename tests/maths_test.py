import maths.arithmetic_progression as ap
import maths.geometric_progression as gp
import maths.factorial as factorial
import maths.fibonacci as fib


def test_ap_get_term() -> bool:
    # the 6th term in an arithmetic progression starting with 0 with a step of
    # 15
    return ap.get_term(6, 0, 15) == 75


def test_ap_get_sum() -> bool:
    # sums the interval [1, 100]
    return ap.get_sum(100, 1, 1) == 5050


def test_gp_get_term() -> bool:
    # the 10th term in a geometric progression starting with 2 with a ratio of 2
    return gp.get_term(10, 2, 2) == 1024


def test_gp_get_sum() -> bool:
    # sums the interval [2, 1024]
    return gp.get_sum(10, 2, 2) == 2046


def test_recursive_factorial() -> bool:
    return factorial.recursive(5) == 120


def test_iterative_factorial() -> bool:
    return factorial.iterative(6) == 720


def test_recursive_fib() -> bool:
    return fib.recursive(6) == 8


def test_iterative_fib() -> bool:
    return fib.iterative(15) == 610


def test_fib_get_sequence() -> bool:
    return fib.get_sequence(6) == [0, 1, 1, 2, 3, 5, 8]


def test_is_fib() -> bool:
    return fib.is_fibonacci(21)


if __name__ == '__main__':
    print(
        f"Get term in A.P.: {'OK' if test_ap_get_term() else 'FAILED'}\n"
        F"Get sum of A.P. sequence: {'OK' if test_ap_get_sum() else 'FAILED'}\n"
        f"Get term in G.P.: {'OK' if test_gp_get_term() else 'FAILED'}\n"
        f"Get sum of G.P.: {'OK' if test_gp_get_sum() else 'FAILED'}\n"
        f"Factorial (Recursive): {'OK' if test_recursive_factorial() else 'FAILED'}\n"
        f"Factorial (Iterative): {'OK' if test_iterative_factorial() else 'FAILED'}\n"
        f"Get Fibonacci number (Recursive): {'OK' if test_recursive_fib() else 'FAILED'}\n"
        f"Get Fibonacci number (Iterative): {'OK' if test_iterative_fib() else 'FAILED'}\n"
        f"Get Fibonacci sequence: {'OK' if test_fib_get_sequence() else 'FAILED'}\n"
        f"Is N in Fibonacci sequence: {'OK' if test_is_fib() else 'FAILED'}"
    )
