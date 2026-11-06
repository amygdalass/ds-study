import sqlite3

import pytest

import sql_assessment as q


def make_db():
    con = sqlite3.connect(":memory:")
    con.executescript(
        """
        CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, group_name TEXT, year INTEGER);
        CREATE TABLE courses (id INTEGER PRIMARY KEY, title TEXT, credits INTEGER);
        CREATE TABLE grades (student_id INTEGER, course_id INTEGER, score INTEGER);

        INSERT INTO students VALUES
            (1, 'Аня', 'БИ-01', 1), (2, 'Борис', 'БИ-01', 1), (3, 'Вера', 'БИ-02', 1),
            (4, 'Глеб', 'БИ-02', 2), (5, 'Дина', 'БИ-03', 2), (6, 'Егор', 'БИ-01', 1);
        INSERT INTO courses VALUES
            (1, 'Матан', 6), (2, 'Линал', 5), (3, 'Python', 4);
        INSERT INTO grades VALUES
            (1, 1, 90), (1, 2, 80), (1, 3, 100),
            (2, 1, 60), (2, 3, 70),
            (3, 2, 50), (3, 3, 95),
            (4, 1, 75);
        """
    )
    return con


def run(sql):
    if not sql.strip():
        pytest.fail("запрос пока пустой")
    return make_db().execute(sql).fetchall()


def test_q1():
    assert run(q.Q1) == [("Аня",), ("Борис",), ("Вера",), ("Егор",)]


def test_q2():
    assert run(q.Q2) == [("БИ-01", 3), ("БИ-02", 2), ("БИ-03", 1)]


def test_q3():
    assert run(q.Q3) == [("Аня", 90.0), ("Глеб", 75.0), ("Вера", 72.5), ("Борис", 65.0)]


def test_q4():
    assert run(q.Q4) == [("Дина",), ("Егор",)]


def test_q5():
    # среднее по всем оценкам = 77.5; Матан 75.0, Линал 65.0, Python 88.3
    assert run(q.Q5) == [("Python",)]
