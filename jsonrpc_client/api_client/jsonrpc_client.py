import tempfile
from django.conf import settings
import requests


def jsonrpc_request(method, params):
    url = "https://slb.medv.ru/api/v2/"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }

    try:
        # Загружаем сертификат и ключ из настроек Django
        cert_data = settings.CERTIFICATE
        key_data = settings.PRIVATE_KEY

        # Отправляем запрос с использованием requests
        response = requests.post(url, json=payload, headers=headers,
                                 cert=(tempfile_data(cert_data), tempfile_data(key_data)))

        # Проверяем успешность запроса
        response.raise_for_status()

        # Получаем и возвращаем результат
        result = response.json()
    except requests.exceptions.RequestException as e:
        result = {"Exception error": str(e)}

    return result


# Функция для создания временных файлов для сертификата и ключа
def tempfile_data(data):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(data.encode('utf-8'))
    temp_file.close()
    return temp_file.name
