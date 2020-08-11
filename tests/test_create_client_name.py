from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestClientName:
    """
    Тестовый класс для проверки позитивных и негативных сценариев
    для введеннего имени клиента в параметре `name`
    ручки `/service/v1/client/create`.
    """

    test_data = GenerateTestData()

    @pytest.mark.parametrize('param_name', test_data.generate_names())
    def test_name_positive(
            self, param_name, create_client_url, user_surname, user_phone):
        """
        Проверка позитивных сценариев для введеного имени.
        """

        _data = {
            'name': param_name,
            'surname': user_surname,
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

    @pytest.mark.parametrize('param_name', test_data.check_neg_names())
    def test_name_negative(
            self, param_name, create_client_url, user_surname, user_phone):
        """
        Проверка негативных сценариев для введеного имени.
        """

        _data = {
            'name': param_name,
            'surname': user_surname,
            'phone': user_phone
        }

        try:
            response = requests.post(create_client_url, json=_data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            assert True, f'HTTP Error: {err}'
        except requests.exceptions.ConnectionError:
            assert False, 'ConnectionError'
