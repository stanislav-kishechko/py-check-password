import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "A1$abcde",
        "Zz9#Zz9#",
        "Valid#123",
        "ABCdef1@",
    ],
    ids=[
        "common_valid",
        "min_length_valid",
        "mixed_chars_valid",
        "valid_with_hash",
        "valid_upper_lower_digit_special",
    ]
)
def test_valid_passwords(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "Short1#",
        "VeryLongPassword1$",
        "Abcdefg#",
        "lowercase9#",
        "ABCdef123",
        "Ukr字符1@",
    ],
    ids=[
        "too_short",
        "too_long",
        "no_digit",
        "no_upper",
        "no_special",
        "invalid_char_unicode",
    ]
)
def test_invalid_passwords(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    "password, expected",
    [
        ("A1@bcdef", True),
        ("Aa1@bcdefghijklm", True),
        ("Aa1@bcdefghijklmn", False),
    ],
    ids=[
        "boundary_exact_8_valid",
        "boundary_exact_16_valid",
        "boundary_17_invalid",
    ]
)
def test_length_boundaries(password: str, expected: bool) -> None:
    assert check_password(password) is expected
