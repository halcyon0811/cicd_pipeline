import pytest


def foo(n):
    if n<=1:
        return 1
    return foo(n-1) + foo(n-2)


def test_fib():
    assert foo(2) == 2 
