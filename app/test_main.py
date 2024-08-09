import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("", True),
    ("Adam", False)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    ), f"Test should return {expected} if given word is isogram"
