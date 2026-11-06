"""Входной тест: SQL (SQLite).

Впиши запрос в каждую строку. Схема — в test_sql_assessment.py (функция make_db):

    students(id, name, group_name, year)
    courses(id, title, credits)
    grades(student_id, course_id, score)   -- score от 0 до 100

Запуск: pytest assessment/test_sql_assessment.py
"""

# 1. Имена студентов 1 курса (year = 1) по алфавиту. Колонка: name.
Q1 = ""

# 2. Сколько студентов в каждой группе. Колонки: group_name, cnt. Порядок: group_name.
Q2 = ""

# 3. Средний балл каждого студента, у которого есть оценки, округлённый до 1 знака.
#    Колонки: name, avg_score. Порядок: avg_score по убыванию, затем name.
Q3 = ""

# 4. Студенты без единой оценки. Колонка: name. Порядок: name.
Q4 = ""

# 5. ★ Курсы, где средний балл выше среднего по всем оценкам.
#    Колонки: title. Порядок: title.
Q5 = ""
