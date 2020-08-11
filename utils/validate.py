from cerberus import Validator


def validate_schema(func):
    """Валидация получаемого ответа"""
    def wrapper(*args, **kwargs):
        _schema, _data = func(*args, **kwargs)
        v = Validator(_schema)
        result = v.validate(_data)
        if not result:
            return v.errors
    return wrapper
