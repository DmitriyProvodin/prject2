import pytest

from rsc.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    'user_input, expected',
    [
        (7000792289606361, '7000 79** **** 6361'),
        (0, '0'),
        ('1234567812345678', 'Некоректный номер карты'),
        ('Word', 'Некоректный номер карты'),
        (None, 'Некоректный номер карты'),
    ]
)
def test_get_mask_card_number(user_input: int, expected: str) -> None:
    assert  get_mask_card_number(user_input) == expected


@pytest.mark.parametrize(
    [
        (73654108430135874305, '**4305'),
        ('123456789123456789', 'Некоректный номер аккаунта'),
        (1234, 'Некоректный номер аккаунта'),
        ('Word', 'Некоректный номер аккаунта'),
        (None, 'Некоректный номер аккаунта'),
    ]
)
def test_get_mask_account(user_input: int, expented: str) -> None:
    assert get_mask_account(user_input) == expented

