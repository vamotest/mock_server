from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestOrderPrice:
    """
    Тестовый класс для проверки позитивных и негативных сценариев
    для введенной цены `item_id` при оформлении заказа в параметре
    `items.price` ручки `/service/v1/order/create`.
    """
    test_data = GenerateTestData()

    @pytest.mark.parametrize('param_order_price', test_data.generate_prices())
    def test_price_positive(
            self, param_order_price, create_order_url, user_client_id,
            user_address, user_phone, order_item_id, order_quantity):
        """
        Проверка позитивных сценариев для введенной цены `item_id`
        при создании заказа.
        """

        _data = {
            'client_id': user_client_id,
            'address': user_address,
            'phone': user_phone,
            'items': [
                {
                    'item_id': order_item_id,
                    'price': param_order_price,
                    'quantity': order_quantity,
                }
            ]
        }

        try:
            response = requests.post(create_order_url, json=_data)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as err:
            assert False, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
        server_response = ServerResponse()
        server_response.validate_create_order(response)

    @pytest.mark.parametrize('param_order_price', test_data.check_neg_prices())
    def test_price_negative(
            self, param_order_price, create_order_url, user_client_id,
            user_address, user_phone, order_item_id, order_quantity):
        """
        Проверка негативных сценариев для введенной цены `item_id`
        при создании заказа.
        """

        _data = {
            'client_id': user_client_id,
            'address': user_address,
            'phone': user_phone,
            'items': [
                {
                    'item_id': order_item_id,
                    'price': param_order_price,
                    'quantity': order_quantity,
                }
            ]
        }

        try:
            response = requests.post(create_order_url, json=_data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            assert True, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
