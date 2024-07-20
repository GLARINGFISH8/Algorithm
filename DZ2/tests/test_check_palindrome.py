# Аспекты
# Корректная работа с разными типами данных
# Корректность работы реверса
# Корректная работа с размерностью данных
import pytest
from src.main4 import check_palindrome

@pytest.mark.POL_check_palindrome
@pytest.mark.parametrize("n, extend", [(100, False),
                                       (101, True),
                                       (-101, False)])

def test_check_palindromeP(n, extend):
    assert check_palindrome(n) == extend


@pytest.mark.BOUN_check_palindrome
@pytest.mark.parametrize("n, extend", [(0, True),
                                       (1000000000000000000000, False)])

def test_check_palindromeB(n, extend):
    assert check_palindrome(n) == extend




@pytest.mark.NEG_check_palindrome
@pytest.mark.parametrize("n, extend", [(4.5, pytest.raises(TypeError)),
                                       ("101", pytest.raises(TypeError))])

def test_check_palindromeP(n, extend):
    with extend:
        assert check_palindrome(n) == extend