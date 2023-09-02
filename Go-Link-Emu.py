import requests
URL = input("Ссылка: ")
while True:
    try:
        requests.get(URL)
        print("Запрос отравлен!")
    except requests.exceptions.ConnectionError:
        print("Ошибка отправки!")
