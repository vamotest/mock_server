from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestClientSurname:
    """
    Тестовый класс для проверки позитивных и негативных сценариев
    для введенной фамилии клиента в параметре `surname`
    ручки `/service/v1/client/create`.
    """

    test_data = GenerateTestData()

    @pytest.mark.parametrize('param_surname', test_data.generate_surnames())
    def test_surname_positive(
            self, param_surname, create_client_url, user_name, user_phone):
        """
        Проверка позитивных сценариев для введеной фамилии.
        """

        _data = {
            'name': user_name,
            'surname': param_surname,
            'phone': user_phone
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

    @pytest.mark.parametrize('param_surname', test_data.check_neg_surnames())
    def test_surname_negative(
            self, param_surname, create_client_url, user_name, user_phone):
        """
        Проверка негативных сценариев для введеной фамилии.
        """

        _data = {
            'name': user_name,
            'surname': param_surname,
            'phone': user_phone
        }

        try:
            response = requests.post(create_client_url, json=_data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            assert True, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
