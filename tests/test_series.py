from math_series.series import lucas,fibonacci,sum_series


#fibonacci

def test_one_fibonacci():
    actual = fibonacci(1)
    expected =1
    assert actual == expected


def test_zero_fibonacci():
   actual = fibonacci(0)
   expected = 0
   assert actual == expected

def test_fibonacci_negative():
       actual = fibonacci(-1)
       expected = 'Enter a number above zero pls'
       assert actual == expected

def test_fibonacci_strings():
    actual = fibonacci("AAAAA")
    expected = 'Enter a number please'
    assert actual == expected

# lucas.
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_negative():
    actual = lucas(-1)
    expected = 'Enter a number above zero pls'
    assert actual == expected

def test_lucas_strings():
        actual = lucas("AAAAA")
        expected = 'Enter a number please'
        assert actual == expected

def test_zero_lucas():
   actual = lucas(0)
   expected = 0
   assert actual == expected


# sum_series tests
def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_six():
    actual = sum_series(6)
    expected = 8
    assert actual == expected
