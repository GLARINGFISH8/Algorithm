# Аспекты
# Корректная работа с разными типами данных
# Корректность счета единиц
# Корректная работ с размерностью данных
import pytest
from src.main3 import count_ones

@pytest.mark.POL_count_ones
@pytest.mark.parametrize("n, extend", [(8, 1),
                                       (15, 4)])

def test_count_onesP(n, extend):
    assert count_ones(n) == extend




@pytest.mark.BOUN_count_ones
@pytest.mark.parametrize("n, extend", [(1, 1),
                                       (100, 3)])

def test_count_onesB(n, extend):
    assert count_ones(n) == extend



@pytest.mark.NEG_count_ones
@pytest.mark.parametrize("n, extend", [(-1, pytest.raises(ValueError)),
                                       (4.5, pytest.raises(TypeError)),
                                       (-3.5, pytest.raises(TypeError)),
                                       ("45", pytest.raises(TypeError))])

def test_count_onesN(n, extend):
    with extend:
        assert count_ones(n) == extend