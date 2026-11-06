import pytest

from example_tasks import reverse_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", "world hello"),
        ("one", "one"),
        ("", ""),
        ("  many   spaces  ", "spaces many"),
    ],
)
def test_reverse_words(text, expected):
    assert reverse_words(text) == expected
