import pytest

from references_tasks import make_grid, remove_negatives, remove_negatives_inplace, transpose


# --- 1. Разминка: make_grid ---

def test_make_grid_shape():
    assert make_grid(2, 3) == [[0, 0, 0], [0, 0, 0]]
    assert make_grid(1, 1, fill="x") == [["x"]]


def test_make_grid_empty():
    assert make_grid(0, 5) == []
    assert make_grid(3, 0) == [[], [], []]


def test_make_grid_rows_are_independent():
    g = make_grid(3, 2)
    g[0][0] = 1
    assert g == [[1, 0], [0, 0], [0, 0]]
    assert g[0] is not g[1]


# --- 2. Основная: remove_negatives / remove_negatives_inplace ---

@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, -2, 3], [1, 3]),
        ([-1, -2, 3, -4, -5], [3]),
        ([-1, -2], []),
        ([], []),
        ([0, 5], [0, 5]),
    ],
)
def test_remove_negatives(nums, expected):
    original = list(nums)
    result = remove_negatives(nums)
    assert result == expected
    assert nums == original, "исходный список не должен меняться"
    assert result is not nums, "нужен новый список"


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, -2, 3], [1, 3]),
        ([-1, -2, 3, -4, -5], [3]),
        ([-1, -2], []),
        ([], []),
        ([0, 5], [0, 5]),
    ],
)
def test_remove_negatives_inplace(nums, expected):
    same = nums
    result = remove_negatives_inplace(nums)
    assert result is None, "функция «на месте» возвращает None, как list.sort()"
    assert nums == expected
    assert nums is same


def test_inplace_seen_through_alias():
    a = [5, -1, -1, 7]
    b = a
    remove_negatives_inplace(a)
    assert b == [5, 7]


# --- 3. Со звёздочкой: transpose ---

def test_transpose_square():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_transpose_rectangular():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_transpose_empty():
    assert transpose([]) == []


def test_transpose_does_not_touch_original():
    m = [[1, 2], [3, 4]]
    t = transpose(m)
    t[0][0] = 99
    assert m == [[1, 2], [3, 4]]


def test_transpose_twice_is_identity():
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(transpose(m)) == m
