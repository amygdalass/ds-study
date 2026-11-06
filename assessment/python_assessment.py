"""Входной тест: практика по Python и алгоритмам.

Пиши код вместо `raise NotImplementedError`. Сигнатуры и имена не меняй.
Задачи идут от простых к сложным; ★ — со звёздочкой.
Запуск тестов:  pytest assessment/test_python_assessment.py
Одна задача:    pytest assessment -k top_words
"""


# 1. Разминка. Количество гласных (латиница, a e i o u, регистр не важен).
# count_vowels("Hello World") == 3
def count_vowels(text: str) -> int:
    raise NotImplementedError


# 2. Второе по величине РАЗЛИЧНОЕ число. Если такого нет — None.
# second_largest([3, 1, 3, 2]) == 2;  second_largest([5, 5]) is None
# Не сортируй список: один проход, O(n).
def second_largest(nums: list[int]) -> int | None:
    raise NotImplementedError


# 3. k самых частых слов. Регистр не важен, слова — последовательности букв
# (знаки препинания и цифры — разделители). При равной частоте — по алфавиту.
# top_words("The cat and the hat. THE end!", 2) == ["the", "and"]
def top_words(text: str, k: int) -> list[str]:
    raise NotImplementedError


# 4. Правильная скобочная последовательность из ()[]{}; другие символы игнорируй.
# is_balanced("a(b[c]{d})") is True;  is_balanced("(]") is False
def is_balanced(s: str) -> bool:
    raise NotImplementedError


# 5. Два индекса i < j, такие что nums[i] + nums[j] == target, или None.
# Если пар несколько — с наименьшим j. Нужно O(n), не O(n²).
# two_sum([2, 7, 11, 15], 9) == (0, 1)
def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    raise NotImplementedError


# 6. Бинарный поиск: индекс ПЕРВОГО вхождения x в отсортированном списке, или -1.
# Модуль bisect не используй. first_index([1, 2, 2, 2, 3], 2) == 1
def first_index(arr: list[int], x: int) -> int:
    raise NotImplementedError


# 7. Слить пересекающиеся отрезки [a, b] (касание [1,2] и [2,3] — тоже пересечение).
# Вход не отсортирован; верни отсортированный список, исходный не меняй.
# merge_intervals([[1, 3], [8, 10], [2, 6]]) == [[1, 6], [8, 10]]
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError


# 8. Сколькими способами подняться на n ступенек шагами по 1 или 2.
# climb_stairs(0) == 1, climb_stairs(3) == 3. Должно работать быстро при n = 90.
def climb_stairs(n: int) -> int:
    raise NotImplementedError


# 9. Произведение матриц (списки списков) без numpy.
# Если размеры не согласованы — ValueError.
# matmul([[1, 2]], [[3], [4]]) == [[11]]
def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    raise NotImplementedError


# 10. ★ Класс Vector.
#   Vector(1, 2, 3)            — любое число координат
#   len(v), v == w, repr(v) == "Vector(1, 2, 3)"
#   v + w                      — покоординатно; разные размерности -> ValueError
#   v * 2 и 2 * v              — умножение на число
#   v.dot(w)                   — скалярное произведение
#   abs(v)                     — длина (евклидова норма)
#   Vector неизменяемый: v + w возвращает новый объект, v не меняется.
class Vector:
    pass
