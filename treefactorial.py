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
    """Pure Python binomial coefficient, using treefactorial."""
    return int(factorial(n)/(factorial(k)*factorial(n - k)))


if __name__ == '__main__':
    for integer in range(100, -1, -1):
        print(integer, factorial(integer))
