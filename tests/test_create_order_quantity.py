from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import pytest
import requests


class TestOrderQuantity:
	"""
	Тестовый класс для проверки позитивных и негативных сценариев
	для введенного количества товаров при оформлении заказа
	в параметре	`items.quantity` ручки `/service/v1/order/create`.
	"""

	test_data = GenerateTestData()

	@pytest.mark.parametrize(
		'param_order_quantity', test_data.generate_quantities())
	def test_quantity_positive(
			self, param_order_quantity, create_order_url, user_client_id,
			user_address, user_phone, order_item_id, order_price):
		"""
		Проверка позитивных сценариев для введенного количества товаров
		при создании заказа.
		"""

		_data = {
			'client_id': user_client_id,
			'address': user_address,
			'phone': user_phone,
			'items': [
				{
					'item_id': order_item_id,
					'price': order_price,
					'quantity': param_order_quantity,
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
		'param_order_quantity', test_data.check_neg_quantities())
	def test_quantity_negative(
			self, param_order_quantity, create_order_url, user_client_id,
			user_address, user_phone, order_item_id, order_price):
		"""
		Проверка негативных сценариев для введенного количества товаров
		при создании заказа.
		"""

		_data = {
			'client_id': user_client_id,
			'address': user_address,
			'phone': user_phone,
			'items': [
				{
					'item_id': order_item_id,
					'price': order_price,
					'quantity': param_order_quantity,
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
