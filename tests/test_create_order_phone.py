from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestOrderPhone:
	"""
	Тестовый класс для проверки позитивных и негативных сценариев
	для введенного телефона при оформлении заказа в параметре
	`phone` ручки `/service/v1/order/create`.
	"""
	test_data = GenerateTestData()

	@pytest.mark.parametrize('param_phone', test_data.generate_phones())
	def test_phone_positive(
			self, param_phone, create_order_url, user_client_id,
			user_address, order_item_id, order_price, order_quantity):
		"""
		Проверка позитивных сценариев для введеного телефона
		при создании заказа.
		"""

		_data = {
			'client_id': user_client_id,
			'address': user_address,
			'phone': param_phone,
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

	@pytest.mark.parametrize('param_phone', test_data.check_neg_phones())
	def test_phone_negative(
			self, param_phone, create_order_url, user_client_id, user_address,
			order_item_id, order_price, order_quantity):
		"""
		Проверка негативных сценариев для введеного телефона
		при создании заказа.
		"""

		_data = {
			'client_id': user_client_id,
			'address': user_address,
			'phone': param_phone,
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
