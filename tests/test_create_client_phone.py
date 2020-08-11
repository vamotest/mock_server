from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestClientPhone:
    """
    Тестовый класс для проверки позитивных и негативных сценариев
    для введенного телефона клиента в параметре `phone`
    ручки `/service/v1/client/create`.
    """

    test_data = GenerateTestData()

    @pytest.mark.parametrize('param_phone', test_data.generate_phones())
    def test_positive(
            self, param_phone, create_client_url, user_name, user_surname):
        """
        Проверка позитивных сценариев для введеной телефона.
        """

        _data = {
            'name': user_name,
            'surname': user_surname,
            'phone': param_phone
        }

        try:
            response = requests.post(create_client_url, json=_data)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as err:
            assert False, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
        server_response = ServerResponse()
        server_response.validate_create_user(response)

    @pytest.mark.parametrize('params_phone', test_data.check_neg_phones())
    def test_negative(
            self, params_phone, create_client_url, user_name, user_surname):
        """
        Проверка негативных сценариев для введеной номера.
        """

        _data = {
            'name': user_name,
            'surname': user_surname,
            'phone': params_phone
        }

        try:
            response = requests.post(create_client_url, json=_data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            assert True, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'


