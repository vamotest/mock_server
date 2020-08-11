from utils.validate_user_request import UserRequest

from datetime import datetime as dt
from flask import Flask, json, request
import random


api = Flask(__name__)
user_request = UserRequest()


@api.route('/', methods=['GET'])
def index():
	return 'Test task for Voximplant'


@api.route('/service/v1/client/create', methods=['POST'])
def create_user():
	_data = request.json

	response = user_request.validate_create_user(_data)
	if isinstance(response, dict):
		return json.dumps(response), 400

	response = {
		'client_id': random.randint(10000, 99999),
	}

	return json.dumps(response, sort_keys=False), 201


@api.route('/service/v1/order/create', methods=['POST'])
def create_order():
	_data = request.json

	response = user_request.validate_create_order(_data)
	if isinstance(response, dict):
		return json.dumps(response), 400

	response = {
		"order_id": random.randint(10000, 99999),
		"order_number": str(random.randint(10000, 99999))
	}

	return json.dumps(response, sort_keys=False), 201


@api.route('/service/v1/item/purchase/by-client', methods=['POST'])
def show_client_purchase_item():
	_data = request.json

	response = user_request.validate_client_purchase_item(_data)
	if isinstance(response, dict):
		return json.dumps(response), 400

	now = dt.now()
	response = {
		"items": [
			{
				"item_id": str(random.randint(10000, 99999)),
				"purchased": random.choice([True, False]),
				"last_order_number": str(random.randint(10000, 99999)),
				"last_purchase_date": now.strftime("%Y-%m-%dT%H:%M:%S:00Z"),
				"purchase_count": str(random.randint(1, 20))
			}
		]
	}

	return json.dumps(response, sort_keys=False), 201


if __name__ == '__main__':
	api.run()
