from utils.validate import validate_schema


class ServerResponse:

    @validate_schema
    def validate_create_user(self, data):
        """
        Валидация ответа mock-сервера для ручки `/service/v1/client/create`.
        """
        schema = {
            'client_id': {"type": "integer"}
        }
        return schema, data

    @validate_schema
    def validate_create_order(self, data):
        """
        Валидация ответа mock-сервера для ручки `/service/v1/order/create`.
        """
        schema = {
            'order_id': {"type": "integer"},
            'order_number': {'type': 'string'}
        }
        return schema, data

    @validate_schema
    def validate_purchase_by_client(self, data):
        """
        Валидация ответа mock-сервера для ручки
        `service/v1/item/purchase/by-client`
        """
        schema = {
            'items': {
                "type": "list",
                'schema': {
                    'type': 'dict',
                    "schema": {
                        'item_id': {'type': 'string'},
                        'purchased': {'type': 'boolean'},
                        'last_order_number': {'type': 'string'},
                        'last_purchase_date': {'type': 'datetime'},
                        'purchase_count': {'type': 'string'}
                    }
                }
            }
        }
        return schema, data
