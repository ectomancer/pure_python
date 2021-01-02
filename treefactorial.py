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

'''def range_prod(low, high):
    """Pure Python code, no imports by Daniel Fischer @stackoverflow.com
    Daniel Fischer says algorithm is old.
    """
    if low + 1 < high:
        mid = (low + high) // 2
        return range_prod(low, mid)*range_prod(mid + 1, high)
    if low == high:
        return low
    return low*high


def treefactorial(num):
    """Calculate factorial.
    Pure Python code, no imports by Daniel Fischer @stackoverflow.com
    Daniel Fischer says algorithm is old.
    """
    if num < 2:
        return 1
    return range_prod(1, num)

factorial = treefactorial'''
if __name__ == '__main__':
    for integer in range(100, -1, -1):
        print(integer, factorial(integer))
