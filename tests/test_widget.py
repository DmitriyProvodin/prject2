import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    'user_input, expected',
    [
        ('Visa_Platinum 2131231284932299', 'Visa_Platinum 213123******2299')
    ]
)

def test_mask_account_card(user_input, expected):
    assert mask_account_card(user_input) == expected



@pytest.mark.parametrize(
    'user_input, expected',
    [
        ('Visa 7000792289606361', 'Visa 700079******6361'),
        ('Mir 7289094321672902', 'Mir 728909******2902'),
        ('Счёт 8432014830921482304', 'Счёт **2304'),
    ]
)

def uni_mask_account_card(user_input, expected):
    assert mask_account_card(user_input) == expected