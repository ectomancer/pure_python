from typing import TypeVar

Numeric = TypeVar('Numeric', int, float, complex)
EMPTY_SUM = 0
MINUS_ONE = -1

def treefactorial(high: int, low: int=None) -> int:
    """Pure Python factorial, no imports by Daniel Fischer @stackoverflow.com
    Daniel Fischer says algorithm is old.
    """
    if high < 2:
        return 1
    if low is None:
        return treefactorial(high, 1)
    if low + 1 < high:
        mid: int= (low + high) // 2
        return treefactorial(mid, low)*treefactorial(high, mid + 1)
    if low == high:
        return low
    return low*high


factorial = treefactorial


def binom(n: int, k: int) -> int:
    """Pure Python binomial coefficient using treefactorial."""
    return factorial(n)//(factorial(k)*factorial(n - k))


def _subfactorial1(n: int) -> int:
    """Pure Python subfactorial.
    Also called derangement number or de Montmort number or rencontres numbers.
    Published by Remond de Montmort in 1713.
    """
    sum = EMPTY_SUM
    for i in range(n + 1):
        sum += MINUS_ONE**i/factorial(i)
    return round(factorial(n)*sum)


def _subfactorial(n: int) -> int:
    """Pure Python subfactorial.
    Also called derangement number or de Montmort number or rencontres numbers.
    Published by Remond de Montmort in 1713.
    """
    if not n:
        #return round(factorial(n)*MINUS_ONE**0/factorial(0)) #cutdown version of _subfactorial for n=0
        return _subfactorial1(n)
    sum = EMPTY_SUM
    for i in range(1, n + 1):
        sum += binom(n, i)*_subfactorial(n - i)
    return factorial(n) - sum


def subfactorial(number: int) -> int:
    """Pure Python subfactorial.
    Also called derangement number or de Montmort number or rencontres numbers.
    Published by Remond de Montmort in 1713.
    Algorithm using recurrence by Euler.
    """
    result = list()
    for n in range(11):
        result += [_subfactorial(n)]
    if number < 11:
        return result[number]
    for n in range(11, number + 1):
        result += [(n - 1)*(result[n - 2] + result[n - 1])]
    return result[number]


if __name__ == '__main__':
    for integer in range(100, -1, -1):
        print(integer, factorial(integer))
    for n in range(52):
        print(n, subfactorial(n))
