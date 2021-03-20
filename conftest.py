from utils.generate_test_data import GenerateTestData

import random
import uuid
import pytest

fake = GenerateTestData().fake


def format_url(api_url):
    url = f'http://mock-server:5000/service/v1/{api_url}/'
    return url.format(api_url)


@pytest.fixture()
def create_client_url():
    """
    Фикстура отдает URL для создания нового клиента.
    """
    return format_url('client/create')


@pytest.fixture()
def create_order_url():
    """
    Фикстура отдает URL для создания нового заказа.
    """
    return format_url('order/create')


@pytest.fixture()
def create_purchase_client_items_url():
    """
    Фикстура отдает URL для проверки сколько раз клиент покупал/не покупал
    конкретные `item_id` (из запроса), номер последнего заказа
    и дату его создания.
    """
    return format_url('item/purchase/by-client')


@pytest.fixture()
def user_name():
    """
    Фикстура отдает корректное имя клиента.
    """
    return fake.first_name()


@pytest.fixture()
def user_surname():
    """
    Фикстура отдает корректную фамилию клиента.
    """
    return fake.last_name()


@pytest.fixture()
def user_phone():
    """
    Фикстура отдает корректный номер клиента.
    """
    return fake.phone_number()


@pytest.fixture()
def user_address():
    """
    Фикстура отдает корректный адрес клиента.
    """
    return fake.address()


@pytest.fixture()
def order_item_id():
    """
    Фикстура отдает случайное значение `item_id` в заданном диапозоне.
    """
    return random.randint(10000, 99999)


@pytest.fixture()
def order_price():
    """
    Фикстура отдает случайное значение `price` в заданном диапозоне.
    """
    return float(random.randint(100, 1000))


@pytest.fixture()
def order_quantity():
    """
    Фикстура отдает случайное значение количества товара в заданном диапозоне.
    """
    return random.randint(1, 20)


@pytest.fixture()
def user_client_id():
    """
    Фикстура отдает случайной `client_id`.
    """
    return uuid.uuid4().int
