from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import random

import pytest
import requests


class TestOrderItemId:
    """
    Тестовый класс для проверки позитивных и негативных сценариев
    для введенного `item_id` товара при оформлении заказа
    в параметре	`items.item_id` ручки `/service/v1/order/create`.
    """
    test_data = GenerateTestData()

    @pytest.mark.parametrize(
        'param_order_item_id', test_data.generate_item_ids())
    def test_item_id_positive(
            self, param_order_item_id, create_order_url, user_client_id,
            user_address, user_phone, order_price, order_quantity):
        """
        Проверка позитивных сценариев для введенного количества `item_id`
        при создании заказа.
        """

        _data = {
            'client_id': user_client_id,
            'address': user_address,
            'phone': user_phone,
            'items': [
                {
                    'item_id': param_order_item_id,
                    'price': order_price,
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

    @pytest.mark.parametrize(
        'item_ids_length', [number for number in range(2, 11, 1)])
    def test_item_ids_different_length_positive(
            self, user_client_id, user_address, user_phone, item_ids_length):
        """
        Проверка позитивных сценариев для введенного количества нескольких
        `item_id` при создании заказа.
        """

        _data = {
            'client_id': user_client_id,
            'address': user_address,
            'phone': user_phone,
            'items': []
        }

        for item_id in range(item_ids_length):
            _data['items'].append({})
            _data['items'][item_id].update({
                'item_id': random.randint(10000, 99999),
                'price': float(random.randint(100, 1000)),
                'quantity': random.randint(1, 20)
            }
            )

        items = [item['item_id'] for number, item in enumerate(_data['items'])]
        count = dict(
            (x, items.count(x))
            for x in set(items)
            if items.count(x) > 1
        )

        if not count:
            assert True, 'Different item_ids'
        elif len(count.values()) > 1:
            assert False, 'Same item_ids'
        elif list(count.values())[0] > 1:
            assert False, 'Same item_ids'

    @pytest.mark.parametrize(
        'param_order_item_id', test_data.check_neg_item_ids())
    def test_item_id_negative(
            self, param_order_item_id, create_order_url, user_client_id,
            user_address, user_phone, order_price, order_quantity):
        """
        Проверка негативных сценариев для введенного количества `item_id`
        при создании заказа.
        """

        _data = {
            'client_id': user_client_id,
            'address': user_address,
            'phone': user_phone,
            'items': [
                {
                    'item_id': param_order_item_id,
                    'price': order_price,
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

    @pytest.mark.parametrize(
        'item_ids_length', [number for number in range(2, 10, 2)])
    def test_item_ids_different_length_negative(
            self, user_client_id, order_item_id, user_address, user_phone,
            item_ids_length):
        """
        Проверка негативных сценариев для введенного количества нескольких
        `item_id` при создании заказа.
        """

        _data = {
            'client_id': user_client_id,
            'address': user_address,
            'phone': user_phone,
            'items': []
        }

        for item_id in range(item_ids_length):
            _data['items'].append({})
            _data['items'][item_id].update({
                'item_id': order_item_id,
                'price': float(random.randint(100, 1000)),
                'quantity': random.randint(1, 20)
            }
            )

        items = [item['item_id'] for number, item in enumerate(_data['items'])]
        count = dict(
            (x, items.count(x))
            for x in set(items)
            if items.count(x) > 1
        )

        if len(count) > 1:
            assert True, 'Same item_ids'
        elif list(count.values())[0] > 1:
            assert True, 'Same item_ids'
        elif not count:
            assert False, 'Different item_ids'
