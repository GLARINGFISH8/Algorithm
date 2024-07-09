# Аспекты
# Корректная работа с разными типами данных
# Корректная работа с размерностью данных
# Корректность счета
import pytest
from src.TASK_NOM2 import len_Often

@pytest.mark.POL_len_Often
@pytest.mark.parametrize("lst, res", [([1, 2, 3, 3], 3),
                                      ([1, 1, 1, 2, 2, 2], 1)])

def test_len_OftenP(lst, res):
    assert len_Often(lst) == res



@pytest.mark.BOUN_len_Often
@pytest.mark.parametrize("lst, res", [([10, 10, 10, 10, 20, 20, 20], 10)])

def test_len_OftenB(lst, res):
    assert len_Often(lst) == res


@pytest.mark.NEG_len_Often
@pytest.mark.parametrize("lst, res", [({1, 2, 3}, pytest.raises(TypeError)),
                                      (1, pytest.raises(TypeError)),
                                      ([ ], pytest.raises(ValueError))])

def test_len_OftenN(lst, res):
    with res:
        assert len_Often(lst) == res



