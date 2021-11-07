# pascals triangle
from math import factorial


def pascals_triangle(n: int):
    """
    Prints out the first n rows of Pascal's triangle

    Example (n = 5):

    1	 5	 10	 10	 5	 1
    1	 4	 6	 4	 1
    1	 3	 3	 1
    1	 2	 1
    1	 1
    1
    """
    def n_choose_k(n, k):
        num = factorial(n)
        denom = factorial(k) * factorial(n - k)
        return int(num / denom)

    if n == 0:
        print(1)
        return
    else:
        numbers = [f"{n_choose_k(n, i)}\t" for i in range(0, n + 1)]
        print(*numbers)
        return pascals_triangle(n - 1)

print('\n')
pascals_triangle(5)
