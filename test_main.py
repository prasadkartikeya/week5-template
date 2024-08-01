def test_greet():
    from main import greet

    assert "abcd" in greet("abcd")
    assert "hello" in greet("hello")
    assert "MyName" in greet("MyName")


def test_sum_of_two():
    from main import sum_of_two

    assert sum_of_two(5, 3) == 8
    assert sum_of_two(-5, -10) == -15
    assert sum_of_two(-2, 2) == 0


def test_max_of_three():
    from main import max_of_three

    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(10, 2, 3) == 10
    assert max_of_three(10, 20, 3) == 20
    assert max_of_three(10, 20, 20) == 20


def test_factorial():
    from main import factorial

    from random import randint
    from math import factorial as real_factorial

    for _ in range(20):
        num = randint(0, 100)
        assert factorial(num) == real_factorial(num)


def test_is_prime():
    from main import is_prime

    assert is_prime(12582917)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(1610612740)
    assert not is_prime(2873)
    assert not is_prime(4)


def test_count_vowels():
    from main import count_vowels

    assert count_vowels("") == 0
    assert count_vowels("hello world") == 3
    assert count_vowels("banana") == 3
    assert count_vowels("aeiou") == 5
    assert count_vowels("bcdfg") == 0
