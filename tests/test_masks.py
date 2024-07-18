import pytest

from rsc.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def right_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


@pytest.mark.parametrize(
    'user_input', 'expected',
    [
        ('700079228960', '7000 79** 8960'),
        ('7000792289606', '7000 79** *960 6'),
        ('70007922896063', '7000 79** **60 63'),
        ('700079228960636', '7000 79** ***0 636'),
        ('7000792289606361', '7000 79** **** 6361'),
        ('70007922896063611', '7000 79** **** *361 1'),
        ('700079228960636111', '7000 79** **** **61 11'),
        ('7000792289606361111', '7000 79** **** ***1 111'),
        ('70007922896063611111', '7000 79** **** **** 1111')
    ]
)
def len_get_mask_card_number(user_input, expected):
    assert get_mask_card_number(user_input) == expected

@pytest.fixture
def empty_get_mask_card_number():
    assert get_mask_card_number('') == 'Вы указали пустую строку, введите номер карты'

@pytest.mark.parametrize(
    'user_input, expected',
    [('73654108430135874305', '** 4305'), ('73654108430135854893', '** 4893')],
)
def right_get_mask_account(user_input, expected):
    assert get_mask_account(user_input) == expected