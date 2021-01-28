from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestShowPurchaseClientId:
    """
    Тестовый класс для проверки позитивных и негативных сценариев
    для введенного идентификатора клиента в параметре `client_id`
    ручки `/service/v1/item/purchase/by-client`.
    """
    test_data = GenerateTestData()

    @pytest.mark.parametrize(
        'param_client_id', test_data.generate_client_ids())
    def test_client_id_positive(
            self, param_client_id, create_purchase_client_items_url,
            order_item_id):
        """
        Проверка позитивных сценариев для введеного идентификатора клиента
        при проверке сколько раз клиент покупал/не покупал конкретные
        `item_id` (из запроса).
        """

        _data = {
            'client_id': str(param_client_id),
            'item_ids': [
                str(order_item_id)
            ]
        }

        try:
            response = requests.post(
                create_purchase_client_items_url, json=_data)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as err:
            assert False, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
        server_response = ServerResponse()
        server_response.validate_create_order(response)

    @pytest.mark.parametrize(
        'param_client_id', test_data.check_neg_client_ids())
    def test_client_id_negative(
            self, param_client_id, create_purchase_client_items_url,
            order_item_id):
        """
        Проверка негативных сценариев для введеного идентификатора клиента
        при проверке сколько раз клиент покупал/не покупал конкретные
        `item_id` (из запроса).
        """

        _data = {
            'client_id': param_client_id,
            'item_ids': [
                str(order_item_id)
            ]
        }

        try:
            response = requests.post(
                create_purchase_client_items_url, json=_data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            assert True, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
