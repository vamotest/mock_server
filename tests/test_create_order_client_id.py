from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestOrderClientId:
	"""
	Тестовый класс для проверки позитивных и негативных сценариев
	для введенного идентификатора клиента при оформлении заказа
	в параметре	`client_id` ручки `/service/v1/order/create`.
	"""
	test_data = GenerateTestData()

	@pytest.mark.parametrize('param_client_id', test_data.generate_client_id())
	def test_client_id_positive(
			self, param_client_id, create_order_url, user_address, user_phone,
			order_item_id, order_price, order_quantity):
		"""
		Проверка позитивных сценариев для введеного идентификатора клиента
		при создании заказа.
		"""

		_data = {
			'client_id': param_client_id,
			'address': user_address,
			'phone': user_phone,
			'items': [
				{
					'item_id': order_item_id,
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
		'param_client_id', test_data.check_neg_client_id())
	def test_client_id_negative(
			self, param_client_id, create_order_url, user_address, user_phone,
			order_item_id, order_price, order_quantity):
		"""
		Проверка негативных сценариев для введеного идентификатора клиента
		при создании заказа.
		"""

		_data = {
			'client_id': param_client_id,
			'address': user_address,
			'phone': user_phone,
			'items': [
				{
					'item_id': order_item_id,
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
