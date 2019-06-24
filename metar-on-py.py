# Python App by firgzirg, github.com/firgzirg

import requests
import ast
####
def _welcome_():
    print("""
    Metar v.0.1 // metar-py.github.io


    Просмотр метар-данных по ИКАО-коду аэропорта.


    """)
####
_USERENT1 = '' # prepared string for user entered datа

decoded_icao = ''
####

airport_icao = str(_USERENT1) # makes inputed varible
decoded_icao = str(airport_icao.lower()) # decodes to lower cap

print(airport_icao)
####
# Running all defines #
_welcome_()
while len(_USERENT1) != 4:
    _USERENT1 = input('Введите ИКАО-код аэропорта : ')
    if(len(_USERENT1) < 4):
        print('Введите верный ИКАО-код!')
    elif(len(_USERENT1) > 4):
        print('Введите верный ИКАО-код!')

airport_icao = str(_USERENT1) # makes inputed varible
decoded_icao = str(airport_icao.lower()) # decodes to lower cap

station_source = "https://api.checkwx.com/metar/"
station_full = station_source + decoded_icao

_api_key_ = { 'X-API-Key': 'YOUR API-KEY' } # api key
_api_req_ = requests.get(station_full, headers=_api_key_)
if(_api_req_ != ''):
    print('[LOG] - Соединение установленно\n')

_nfmetar = ast.literal_eval(_api_req_.text)

_finalmetar = ''.join(_nfmetar['data'])
if(_finalmetar == ''):
    print("Неверный ИКАО-код")

print('Метар-данные получены : ', '\n')
print(_finalmetar + '\n')
#print(decoded_icao)
