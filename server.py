from utils.validate_user_request import UserRequest
from utils.generate_test_data import GenerateTestData

from flask import Flask, json, request


api = Flask(__name__)
user_request = UserRequest()
test_data = GenerateTestData()


@api.route('/', methods=['GET'])
def index():
    """
    Главная страница mock-сервера через метод GET.
    """
    return 'Test task for Voximplant'


@api.route('/service/v1/client/create', methods=['POST'])
def create_user():
    """
    Ручка создания нового пользователя mock-сервера через метод POST.
    """
    _data = request.json

    validation_response = user_request.validate_create_user(_data)
    if isinstance(validation_response, dict):
        return json.dumps(validation_response), 400

    server_response = {
        'client_id': test_data.generate_client_id(),
    }

    return json.dumps(server_response, sort_keys=False), 201


@api.route('/service/v1/order/create', methods=['POST'])
def create_order():
    """
    Ручка создания нового заказа пользователя mock-сервера через метод POST.
    """
    _data = request.json

    validation_response = user_request.validate_create_order(_data)
    if isinstance(validation_response, dict):
        return json.dumps(validation_response), 400

    server_response = {
        'order_id': test_data.generate_client_id(),
        'order_number': test_data.generate_order_number()
    }

    return json.dumps(server_response, sort_keys=False), 201


@api.route('/service/v1/item/purchase/by-client', methods=['POST'])
def show_client_purchase_item():
    """
    Ручка для проверки сколько раз клиент покупал/не покупал конкретные
    item_id (из запроса) mock-сервера через метод POST.
    """
    _data = request.json

    response = user_request.validate_client_purchase_item(_data)
    if isinstance(response, dict):
        return json.dumps(response), 400

    server_response = {
        'items': []
    }

    for item, item_id in enumerate(_data['item_ids']):
        server_response['items'].append({})
        server_response['items'][item].update(
            {
                'item_id': str(test_data.generate_id()),
                'purchased': test_data.generate_boolean(),
                'last_order_number': test_data.generate_order_number(),
                'last_purchase_date': test_data.generate_datetime(),
                'purchase_count': str(test_data.generate_quantity())
            }
        )

    return json.dumps(server_response, sort_keys=False), 201


if __name__ == '__main__':
    api.run(host='0.0.0.0')
