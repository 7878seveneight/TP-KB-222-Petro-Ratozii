import pytest
from lab04 import *

operators = {'+', '-', '*', '/', '^'}

def test1():
    tokens = ["2","3","+"]
    result = zpz(tokens)
    assert result == 5

def test2():
    tokens = ["16", "/", "(","5","3","-",")", "3", "^"]
    result = zpz(tokens)
    assert result == 2

def test3():
    tokens = ["2", "5", "*", "(", "4", "5", "*", "3", "^", ")", "*"]
    result = zpz(tokens)
    assert result == 5000

def test4():
    tokens = ["(", "2", "5", "*", "(", "4", "5", "*", "3", "^", ")", "*", ")", "100", "/"]
    result = zpz(tokens)
    assert result == 50

if __name__ == "__main__":
    pytest.main()