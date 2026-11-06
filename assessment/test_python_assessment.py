import math

import pytest

from python_assessment import (
    Vector,
    climb_stairs,
    count_vowels,
    first_index,
    is_balanced,
    matmul,
    merge_intervals,
    second_largest,
    top_words,
    two_sum,
)


# 1
@pytest.mark.parametrize(
    ("text", "expected"),
    [("Hello World", 3), ("", 0), ("xyz", 0), ("AEIOUaeiou", 10), ("Привет, mir", 1)],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


# 2
@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([3, 1, 3, 2], 2),
        ([5, 5], None),
        ([], None),
        ([7], None),
        ([-1, -5, -3], -3),
        ([1, 2, 3, 4, 5], 4),
        ([10, 9, 10, 9], 9),
    ],
)
def test_second_largest(nums, expected):
    assert second_largest(nums) == expected


def test_second_largest_does_not_modify_input():
    nums = [3, 1, 2]
    second_largest(nums)
    assert nums == [3, 1, 2]


# 3
@pytest.mark.parametrize(
    ("text", "k", "expected"),
    [
        ("The cat and the hat. THE end!", 2, ["the", "and"]),
        ("b a c b a", 3, ["a", "b", "c"]),
        ("one", 5, ["one"]),
        ("", 3, []),
        ("x1y2x", 1, ["x"]),
        ("Да, да! Нет.", 1, ["да"]),
    ],
)
def test_top_words(text, k, expected):
    assert top_words(text, k) == expected


# 4
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("a(b[c]{d})", True),
        ("", True),
        ("(]", False),
        ("((", False),
        ("))((", False),
        ("([)]", False),
        ("{[()()]}", True),
        ("text without brackets", True),
    ],
)
def test_is_balanced(s, expected):
    assert is_balanced(s) is expected


# 5
@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 3], 6, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([1, 2, 3], 7, None),
        ([], 0, None),
        ([5], 10, None),
        ([-1, 0, 1, 2], 1, (1, 2)),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


def test_two_sum_is_fast():
    nums = list(range(200_000))
    assert two_sum(nums, 399_997) == (199_998, 199_999)


# 6
@pytest.mark.parametrize(
    ("arr", "x", "expected"),
    [
        ([1, 2, 2, 2, 3], 2, 1),
        ([1, 2, 3], 4, -1),
        ([1, 2, 3], 0, -1),
        ([], 1, -1),
        ([5], 5, 0),
        ([1, 1, 1, 1], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
    ],
)
def test_first_index(arr, x, expected):
    assert first_index(arr, x) == expected


def test_first_index_big():
    arr = [0] * 500_000 + [1] * 500_000
    assert first_index(arr, 1) == 500_000


# 7
@pytest.mark.parametrize(
    ("intervals", "expected"),
    [
        ([[1, 3], [8, 10], [2, 6]], [[1, 6], [8, 10]]),
        ([[1, 2], [2, 3]], [[1, 3]]),
        ([], []),
        ([[5, 5]], [[5, 5]]),
        ([[1, 10], [2, 3], [4, 5]], [[1, 10]]),
        ([[6, 7], [1, 2], [3, 4]], [[1, 2], [3, 4], [6, 7]]),
    ],
)
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected


def test_merge_intervals_does_not_modify_input():
    intervals = [[2, 6], [1, 3]]
    merge_intervals(intervals)
    assert intervals == [[2, 6], [1, 3]]


# 8
@pytest.mark.parametrize(("n", "expected"), [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (10, 89)])
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected


def test_climb_stairs_fast():
    assert climb_stairs(90) == 4660046610375530309


# 9
def test_matmul_basic():
    assert matmul([[1, 2]], [[3], [4]]) == [[11]]
    assert matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]


def test_matmul_identity():
    a = [[1, 2, 3], [4, 5, 6]]
    eye = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert matmul(a, eye) == a


def test_matmul_non_square():
    assert matmul([[1], [2]], [[3, 4]]) == [[3, 4], [6, 8]]


def test_matmul_shape_mismatch():
    with pytest.raises(ValueError):
        matmul([[1, 2]], [[1, 2]])


# 10
def test_vector_basics():
    v = Vector(1, 2, 3)
    assert len(v) == 3
    assert repr(v) == "Vector(1, 2, 3)"
    assert v == Vector(1, 2, 3)
    assert v != Vector(1, 2)


def test_vector_add_is_new_object():
    v, w = Vector(1, 2), Vector(3, 4)
    s = v + w
    assert s == Vector(4, 6)
    assert v == Vector(1, 2)


def test_vector_add_dim_mismatch():
    with pytest.raises(ValueError):
        Vector(1, 2) + Vector(1, 2, 3)


def test_vector_scalar_mul_both_sides():
    assert Vector(1, -2) * 3 == Vector(3, -6)
    assert 3 * Vector(1, -2) == Vector(3, -6)


def test_vector_dot_and_abs():
    assert Vector(1, 2, 3).dot(Vector(4, 5, 6)) == 32
    assert math.isclose(abs(Vector(3, 4)), 5.0)
