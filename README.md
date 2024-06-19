# JSON-RPC Client

## Описание

Этот проект представляет собой примитивный клиент для взаимодействия с существующим JSON-RPC сервисом. Клиент реализует
функционал авторизации на сервисе, получения и отображения ответов от сервера.

## Функциональные возможности

- Авторизация на JSON-RPC сервисе
- Отправка запросов к сервису
- Получение и отображение ответов от сервера

## Минимальные требования:

- [x] Python
- [x] Poetry
- [x] Django

## Используемые инструменты для разраотки:

|       Tools       | Version |
|:-----------------:|:-------:|
|      python       |  3.11   |
|      poetry       |  1.6.1  |
|      flake8       |  7.1.0  |
|      Django       |  5.0.6  |
| django-bootstrap5 |  24.2   |
|     coverage      |  7.5.3  |

## Быстрый старт

| Step |                                 Instruction                                  |
|:----:|:----------------------------------------------------------------------------:|
|  1   |                        Clone he repository to your PC                        |
|  2   |                     Go to repository<br/>`cd qualixDEV`                      |
|  3   |        Installing the application on your computer<br/>`make install`        | 
|  4   | Run the command to create tables<br/>`make makemigrations` /  `make migrate` | 
|  5   |              To start the Django server, use the<br/>`make dev`              |


## Документации

- [Poetry](https://python-poetry.org)

- [Django](https://www.djangoproject.com/)


#### P.s.

- Вместо дефолтного `SQLite` использовал бы postgres
- Docker для развертки контейнера `postgres` + `dj-database-url` :
```sh
docker run -d \
    --name jsonrpc_db \
    -e POSTGRES_USER=pguser \
    -e POSTGRES_PASSWORD=pgpass \
    -e POSTGRES_DB=pgdb \
    -p 5434:5432 \
    postgres:latest

```
- `.env` в связке с `load_dotenv()` для хранения ключей/токенов 
- Ну и тестиков бы побольше