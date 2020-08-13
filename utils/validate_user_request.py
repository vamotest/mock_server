from utils.validate import validate_schema


class UserRequest:
	"""
	Валидации запросов пользователей к mock-server.
	"""
	@validate_schema
	def validate_create_user(self, _data):
		"""
		Валидация запроса клиента к mock-серверу
		для ручки `/service/v1/client/create`.
		"""
		_schema = {
			'name': {'type': 'string'},
			'surname': {'type': 'string'},
			'phone': {'type': 'string'}
		}
		return _schema, _data

	@validate_schema
	def validate_create_order(self, _data):
		"""
		Валидация запроса клиента к mock-серверу
		для ручки `/service/v1/client/order`.
		"""
		_schema = {
			'client_id': {'type': 'integer'},
			'address': {'type': 'string'},
			'phone': {'type': 'string'},
			'items': {
				'type': 'list',
				'schema': {
					'type': 'dict',
					'schema': {
						'item_id': {'type': 'integer'},
						'price': {'type': 'float'},
						'quantity': {'type': 'integer'}
					}
				}
			}
		}
		return _schema, _data

	@validate_schema
	def validate_client_purchase_item(self, _data):
		"""
		Валидация запроса клиента к mock-серверу
		`service/v1/item/purchase/by-client`.
		"""
		_schema = {
			'client_id': {'type': 'string'},
			'item_ids': {
				'type': 'list',
				'schema': {'type': 'string'}
			}
		}
		return _schema, _data
