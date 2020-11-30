from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series



def test_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_minus():
    actual = fibonacci(-1)
    expected = 'Incorrect input'
    assert actual == expected

def test_five_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_minus_lucas():
    actual = lucas(-1)
    expected = 'Incorrect input'
    assert actual == expected

def test_five_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected   

def test_zero_sum_series():
    actual = sum_series(0,2)
    expected = 2
    assert actual == expected