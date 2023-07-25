import pytest
from conftest import API_URL, mock_api

def test_check_money(user):
    cheap_price = 500
    expensive_price = 10000000


    can_buy = user._check_money_enough(price= cheap_price)

    assert can_buy

    cannot_buy = user._check_money_enough(price= expensive_price)

    assert not cannot_buy
    ...


def test_give_money_cheaper(user):
    price = 500

    pre_money = user._money
    
    user._give_money(money=price)

    assert user._money == pre_money - price


def test_give_money_expensive(user):

    price = 1000000000

    with pytest.raises(Exception):
        assert user._give_money(money=price)


# Interagtion Test
def test_purchase_product_well(mock_api, user, mock_products):
    # 1. 유저가 돈을 잘 냈는가?
    # 2. 유저의 주머니에 상품이 들어 있는가?

    product_id = 1

    pre_user_money = user._money
    user.belongs = []
    mock_product = mock_products[product_id]

    product = user.purchase_product(product_id = product_id)

    assert user.get_money() == pre_user_money - product.price
    assert user.get_belongs() == [product]


def test_purchase_product_not_well(mock_api, user, mock_products):
    # 비싼 상품 구매시

    product_id = 2
    mock_product = mock_products[product_id]
    pre_user_money = user._money

    with pytest.raises(Exception):
        user.purchase_product(product_id = product_id)






    





