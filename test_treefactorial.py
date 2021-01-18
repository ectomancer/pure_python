import math

import sympy

import treefactorial

def test_treefactorial():
    """Test treefactorial with pytest."""
    assert treefactorial.factorial(0) == 1
    assert treefactorial.factorial(1) == 1
    assert treefactorial.factorial(2) == 2
    assert treefactorial.factorial(3) == 6
    assert treefactorial.factorial(4) == 24
    assert treefactorial.factorial(5) == 120
    assert treefactorial.factorial(6) == 720
    assert treefactorial.factorial(7) == 5040
    assert treefactorial.factorial(8) == 40320
    assert treefactorial.factorial(9) == 362880
    assert treefactorial.factorial(10) == 3628800
    for integer in range(11, 101):
        assert treefactorial.factorial(integer) == math.factorial(integer)

def test_subfactorial():
    """Test subfactorial with pytest."""
    for n in range(101):
        assert treefactorial.subfactorial(n) == sympy.functions.combinatorial.factorials.subfactorial(n)
