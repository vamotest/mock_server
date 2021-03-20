import random
from uuid import uuid4
from faker import Faker


class GenerateTestData:
    """
    Класс для получения рандомных и фейковых данных.
    """

    def __init__(self):
        self.nationality = [
            'ar_EG', 'bg_BG', 'bs_BA', 'cs_CZ', 'de_DE', 'dk_DK', 'el_GR',
            'en_US', 'es_ES', 'et_EE', 'fa_IR', 'fi_FI', 'fr_FR', 'hi_IN',
            'hr_HR', 'hu_HU', 'hy_AM', 'it_IT', 'ja_JP', 'ka_GE', 'ko_KR',
            'lt_LT', 'lv_LV', 'ne_NP', 'nl_NL', 'no_NO', 'pl_PL', 'pt_BR',
            'ro_RO', 'ru_RU', 'sl_SI', 'sv_SE', 'tr_TR', 'uk_UA', 'zh_CN'
        ]
        self.fake = Faker(self.nationality)

    def generate_date(self):
        """
        Генератор случайной даты и времени за последние два года
        в заданом формате.
        """
        date = self.fake.date_time_between(start_date='-2y', end_date='now')
        return date.strftime('%Y-%m-%d')

    def generate_datetime(self):
        """
        Генератор случайной даты и времени за последние два года
        в заданом формате.
        """
        datetime = self.fake.date_time_between(
            start_date='-2y', end_date='now')
        return datetime.strftime('%Y-%m-%dT%H:%M:%S:00Z')

    @staticmethod
    def generate_client_id():
        """
        Генератор uuid4 client_id.
        """
        return uuid4().int

    @staticmethod
    def generate_id():
        """
        Генератор случайного id.
        """
        return random.randint(10000, 99999)

    def generate_order_number(self):
        """
        Генератор случайного `order_number` по заданной маске.
        """
        return self.fake.bothify(text='????-########')

    @staticmethod
    def generate_boolean():
        """
        Случайное boolean значение.
        """
        return random.choice([True, False])

    @staticmethod
    def generate_quantity():
        """
        Генератор случайного количества товара.
        """
        return random.randint(1, 20)

    def generate_names(self):
        """
        Генератор имен по заданным национальностям.
        """
        return [self.fake.first_name() for _ in enumerate(self.nationality)]

    def check_neg_names(self):
        """
        Составляем список некорректных форматов имён.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result

    def generate_surnames(self):
        """
        Генератор фамилий по заданным национальностям.
        """
        return [self.fake.last_name() for _ in enumerate(self.nationality)]

    def check_neg_surnames(self):
        """
        Составляем список некорректных форматов фамилий.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result

    def generate_phones(self):
        """
        Генератор номеров телефона разного формата.
        """
        return [self.fake.phone_number() for _ in range(5)]

    def check_neg_phones(self):
        """
        Составляем список некорректных форматов телефона.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result

    def generate_client_ids(self):
        """
        Генератор client_id разной длинны.
        """
        return [self.generate_client_id() for _ in range(5)]

    def check_neg_client_ids(self):
        """
        Составляем список некорректных форматов client_id.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result

    def generate_user_address(self):
        """
        Генератор адресов разного формата.
        """
        return [self.fake.address() for _ in range(5)]

    def check_neg_address(self):
        """
        Составляем список некорректных форматов адресов.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], (),
            'test'
        ]
        return result

    @staticmethod
    def generate_item_ids():
        """
        Генератор item_ids разной длинны.
        """
        return [random.randint(10000, 99999) for _ in range(5)]

    def check_neg_item_ids(self):
        """
        Составляем список некорректных форматов item_id.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result

    @staticmethod
    def generate_prices():
        """
        Генератор разной цены товара.
        """
        return [float(random.randint(100, 1000)) for _ in range(5)]

    def check_neg_prices(self):
        """
        Составляем список некорректных форматов цены товара.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result

    @staticmethod
    def generate_quantities():
        """
        Генератор разного количества товара.
        """
        return [random.randint(1, 20) for _ in range(5)]

    def check_neg_quantities(self):
        """
        Составляем список некорректных форматов количества товара.
        """
        result = [
            self.generate_date(), self.generate_datetime(),
            0, -1, 1.0, '', True, 0b1010, None, {}, [], ()
        ]
        return result
