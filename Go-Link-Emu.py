import requests

send2 = requests.get
send = requests.post

URL = input("Ссылка: ")

while True:
           try:
               send(URL)
               print("Запрос отравлен!")
           except requests.exceptions.ConnectionError:
                                                      print("Ошибка отправки!")

           try:
               send2(URL)
               print("Запрос отравлен!")
           except requests.exceptions.ConnectionError:
                                                      print("Ошибка отправки!")
