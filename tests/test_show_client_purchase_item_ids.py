from utils.generate_test_data import GenerateTestData
from utils.validate_server_response import ServerResponse

import random

import pytest
import requests


class TestShowPurchaseItemsId:
	"""
	Тестовый класс для проверки позитивных и негативных сценариев
	для введенных позиций товара клиента в параметре `item_ids`
	ручки `/service/v1/item/purchase/by-client`.
	"""
	test_data = GenerateTestData()

	@pytest.mark.parametrize(
		'param_item_id', test_data.generate_item_ids())
	def test_client_id_positive(
			self, user_client_id, create_purchase_client_items_url,
			param_item_id):
		"""
		Проверка позитивных сценариев сколько раз клиент покупал/не покупал
		конкретный `item_id` (из запроса).
		"""

		_data = {
			'client_id': str(user_client_id),
			'item_ids': [
				str(param_item_id)
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
		'item_ids_length', [number for number in range(2, 11, 1)])
	def test_client_ids_different_length_positive(
			self, user_client_id, item_ids_length):
		"""
		Проверка позитивных сценариев сколько раз клиент покупал/не покупал
		несколько `item_id` (из запроса).
		"""

		_data = {
			'client_id': str(user_client_id),
			'item_ids': []
		}

		for item_id in range(item_ids_length):
			_data['item_ids'].append(str(random.randint(10000, 99999)))

		count = dict(
			(x, _data['item_ids'].count(x))
			for x in set(_data['item_ids'])
			if _data['item_ids'].count(x) > 1
		)

		if not count:
			assert True, 'Different item_ids'
		elif len(count.values()) > 1:
			assert False, 'Same item_ids'
		elif list(count.values())[0] > 1:
			assert False, 'Same item_ids'

	@pytest.mark.parametrize(
		'param_item_id', test_data.check_neg_item_ids())
	def test_client_id_negative(
			self, param_item_id, user_client_id,
			create_purchase_client_items_url):
		"""
		Проверка негативных сценариев сколько раз клиент покупал/не покупал
		конкретные `item_id` (из запроса), а также пустой `item_id`.
		"""
		_data = {
			'client_id': str(user_client_id),
			'item_ids': [
				param_item_id
			]
		}
		if not _data['item_ids']:
			assert True

		try:
			response = requests.post(
				create_purchase_client_items_url, json=_data)
			response.raise_for_status()
		except requests.exceptions.HTTPError as err:
			assert True, f'HTTP Error: {err}'
		except requests.exceptions.ConnectionError:
			assert False, 'ConnectionError'

	@pytest.mark.parametrize(
		'item_ids_length', [number for number in range(2, 10, 2)])
	def test_client_ids_different_length_negative(
			self, user_client_id, item_ids_length, order_item_id):
		"""
		Проверка негативных сценариев сколько раз клиент покупал/не покупал
		конкретные `item_id` (из запроса).
		"""
		_data = {
			'client_id': str(user_client_id),
			'item_ids': []
		}

		for item_id in range(item_ids_length):
			_data['item_ids'].append(str(order_item_id))
			_data['item_ids'].append(str(order_item_id + 1))

		count = dict(
			(x, _data['item_ids'].count(x))
			for x in set(_data['item_ids'])
			if _data['item_ids'].count(x) > 1
		)

		if len(count) > 1:
			assert True, 'Same item_ids'
		elif list(count.values())[0] > 1:
			assert True, 'Same item_ids'
		elif not count:
			assert False, 'Different item_ids'
