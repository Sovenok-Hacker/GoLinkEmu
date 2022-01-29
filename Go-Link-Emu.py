import requests
send2 = requests.get
URL = input("Ссылка: ")
while True:
    try:
        send(URL)
        print("Запрос отравлен!")
    except requests.exceptions.ConnectionError:
        print("Ошибка отправки!")
