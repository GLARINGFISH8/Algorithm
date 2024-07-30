#Аспекты: Корректность сортировки, Корректность работы с типами данных, Корректность работы с размерностью данных

import pytest

pytest.mark.POL_buble_sorted
pytest.mark.parametrize("array, extend_result", [([2, 1 ,3], [1, 2 ,3]),
                                                 ([1, -2, 3], [-2, 1, 3]),
                                                 ()])


