import sqlite3


def _create_database():
    """
    Создание подключения с БД.
    """
    conn = sqlite3.connect('db.sqlite3')
    return conn


class Sqlite:
    """
    Базовый класс для работы с БД.
    """
    def __init__(self):
        self.conn = _create_database()
        self.cursor = self.conn.cursor()


class SqliteCreateUser(Sqlite):
    """
    Наследник класса Sqlite. Отвечает за работу с таблицей `clients`.
    """
    def __init__(self):
        super().__init__()
        self._create_table()

    def _create_table(self):
        """
        Создание таблицы `clients` при ее отсутствии.
        """
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS clients('
            '"client_id" UNIQUE,'
            '"name" VARCHAR(255),'
            '"surname" VARCHAR(255),'
            '"phone" VARCHAR(255))'
        )

    def write_transaction(self, client_id, name, surname, phone):
        """
        Запись параметров `client_id`, `name`, `surname`, `phone`
        в таблицу `clients`.
        """
        self.cursor.execute(
            'INSERT INTO clients VALUES (?, ?, ?, ?)',
            (client_id, name, surname, phone))
        self.conn.commit()


class SqliteCreateOrder(Sqlite):
    """
    Наследник класса Sqlite. Отвечает за работу с таблицей orders.
    """
    def __init__(self):
        super().__init__()
        self._create_table()

    def _create_table(self):
        """
        Создание таблицы `orders` при ее отсутствии.
        """
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS orders('
            '"item_id" UNIQUE,'
            '"purchased" BOOLEAN,'
            '"last_order_number" VARCHAR(255),'
            '"last_purchase_date" DATETIME,'
            '"purchase_count" VARCHAR(255))'
        )

    def write_transaction(
            self, item_id, purchased, last_order_number,
            last_purchase_date, purchase_count):
        """
        Запись параметров `item_id`, `purchased`, `last_order_number`,
        `last_purchase_date`, `purchase_count` в таблицу `orders`.
        """
        self.cursor.execute(
            'INSERT INTO orders VALUES (?, ?, ?, ?, ?)',
            (item_id, purchased, last_order_number, last_purchase_date,
             purchase_count))
        self.conn.commit()
