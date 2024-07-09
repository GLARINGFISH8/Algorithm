# Аспекты
# Корректная работа с разными типами данных
# Корректная работа с размерностью данных
# Корректность счета
import pytest
from src.TASK_NOM3 import find_Part


@pytest.mark.POL_find_Part
@pytest.mark.parametrize("lst, target, lever, res", [([2, 3, 1], 4, "value", [3, 1]),
                                                     ([2.5, 2.5, 2], 5, "index", [0, 1])])

def test_find_PartP(lst, target, lever, res):
    assert find_Part(lst, target, lever) == res



@pytest.mark.BOUN_find_Part
@pytest.mark.parametrize("lst, target, lever, res", [([10, 20, 40], 60, "value", [20, 40]),
                                                     ([10, 20, 40], 60, "index", [1, 2])])

def test_find_PartB(lst, target, lever, res):
    assert find_Part(lst, target, lever) == res



@pytest.mark.NEG_find_Part
@pytest.mark.parametrize("lst, target, lever, res", [({1, 2, 3}, 5, "value", pytest.raises(TypeError)),
                                                     ([ ], 0, "index", pytest.raises(ValueError)),
                                                     ([12424, 234234, 54252], 246658, "value", pytest.raises(ValueError))])

def test_find_PartN(lst, target, lever, res):
    with res:
        assert find_Part(lst, target, lever) == res
