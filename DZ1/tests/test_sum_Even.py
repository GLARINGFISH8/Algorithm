# Аспекты
# Корректная работа с разными типами данных
# Корректная работа с размерностью данных
# Корректность счета

import pytest
from src.TASK_NOM1 import sum_Even



@pytest.mark.POL_sum_Even
@pytest.mark.parametrize("lst, res", [([1, 2, 3, 4], 6),
                                      ([-1, -2, -3], 1),
                                      ([5, 7, 3], 0)])

def test_sum_EvenP(lst, res):
    assert sum_Even(lst) == res




@pytest.mark.BOUN_sum_Even
@pytest.mark.parametrize("lst, res", [([ ], 0),
                                      ([10, 10, 10, 10, 10, 10], 60),])

def test_sum_EvenB(lst, res):
    assert sum_Even(lst) == res


@pytest.mark.NEG_sum_Even
@pytest.mark.parametrize("lst, res", [({1, 3, 4}, pytest.raises(TypeError)),
                                      ((1, 2, 3), pytest.raises(TypeError)),
                                      (1, pytest.raises(TypeError))])


def test_sum_EvenN(lst, res):
    with res:
        assert sum_Even(lst) == res




