# Test task for Voximplant [![Build Status](https://travis-ci.org/vamotest/voximplant.svg?branch=master)](https://travis-ci.org/vamotest/voximplant)

## Index
1. [Technical requirements](#technical-requirements)
2. [Purchase by client](#purchase-by-client)
3. [Create client](#create-client)
4. [Create order](#create-order)
5. [Test run via containers](#test-run-via-containers)
6. [Parallels tests](pytest-parallel)
7. [Test results](#pytest-html)
8. [TODO](#todo)

**[⬆ Back to Index](#index)**
## Technical requirements
Необходимо написать тесты на абстрактную функцию `service/v1/item/purchase/by-client`. 
Вспомогательные функции, оторые могут потребоваться для реализации тестов - 
`v1/client/create` и `v1/order/create`.

Сделать на свое усмотрение базовую структуру проекта с тестами и выложить 
на любой публичный репозиторий. 
Тесты должны быть написаны на Python(3+) + pytest. 


**[⬆ Back to Index](#index)**
## Purchase by client
`service/v1/item/purchase/by-client` - функция возвращает, сколько раз клиент 
покупал/не покупал конкретные `item_id` (из запроса), номер последнего 
заказа и дату его создания.

**Request:**
```json
{
  "client_id": "string",
  "item_ids": [
    "string"
  ]
}
```

**Response:**
```json
{
  "items": [
    {
      "item_id": "string",
      "purchased": "boolean",
      "last_order_number": "string",
      "last_purchase_date": "2020-01-16T13:33:00.000Z",
      "purchase_count": "string"
    }
  ]
}
```

**[⬆ Back to Index](#index)**
## Create client
`service/v1/client/create` - функция создает клиента.

**Request:**
```json
{
  "name": "string",
  "surname": "string",
  "phone": "string"
}
```
**Response:**
```json
{
  "client_id": "integer"
}
```

**[⬆ Back to Index](#index)**
## Create order
`service/v1/order/create` - функция создает заказ.

**Request:**
```json
{
  "client_id": "integer",
  "address": "string",
  "phone": "string",
  "items": [
    {
      "item_id": "integer",
      "price": "float",
      "quantity": "integer",
    }
  ]
}
```

**Response:**
```json
{
  "order_id": "integer",
  "order_number": "string"
}
```




**[⬆ Back to Index](#index)**
## Test run via containers]
Для запусков тестов в контейнере небходимо иметь предустановленный [Docker](https://www.docker.com/get-started):
```shell script
~ docker-compose up --abort-on-container-exit
```
* Arguments:
```
[--abort-on-container-exit]: stops all containers if any container was stopped.
```


**[⬆ Back to Index](#index)**
## Parallels tests
Для параллельного запуска тестов в [docker-compose](https://github.com/vamotest/voximplant/blob/master/docker-compose.yml#L20) файле необходимо указать:
```shell script
command: python3 -m pytest tests -v --workers auto --tests-per-worker 4 --html=tests/results/report.html
```
* Arguments:
```
[-v], [--verbose]: increase verbosity;
[--workers auto]: runs 4 workers (assuming a quad-core machine);
[--tests-per-worker]: runs 1 worker with 4 tests at a time;
[--html]: generate a HTML report for the test results.
```


**[⬆ Back to Index](#index)**
## Test results
Для просмотра результатов после прогона тестов в контейнере
из корневой директории проекта необходимо выполнить:
```shell script
~ open tests/results/report.html 
```

**[⬆ Back to Index](#index)**
## TODO
- [ ] More tests;
- [ ] Add test helpers;
- [ ] Link DBMS (`in progress`);
- [ ] Improve mock-server.