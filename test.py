import re
import string
import urllib
import time
import sys
import urllib.request
from time import sleep
import requests
from couchdb import Server
from couchdb.design import ViewDefinition
import json
user = 'user'
password = 'pass'
url = 'http://%s:%s@45.113.232.65:5984/'
db_name = 'au_user'
server = Server(url % (user, password))
if db_name in server:
    database = server[db_name]
    print('Login into couchdb database: ', db_name)
else:
    database = server.create(db_name)
    print('Create new couchdb database: ', db_name)

f1=open('au_user.json','r',encoding='UTF-8')
game=json.load(f1)['docs']
for i in game:
    print(i)
    if not i['doc'].__contains__('steamid'):
        continue
    data={
        'steamid':i['doc']['steamid'],
        'country':i['doc']['country'],
        'game_num':i['doc']['game_num'],
        'review_num':i['doc']['review_num'],
        'from_game':i['doc']['from_game'],
        'total_time':i['doc']['total_time'],
        'recent_time':i['doc']['recent_time'],
        'last_played':i['doc']['last_played'],
        'type':i['doc']['type'],
    }
    if i['doc'].__contains__('state'):
        i['state']=i['doc']['state']
    if i['doc'].__contains__('city'):
        i['state']=i['doc']['city']
    print(data)
    database.save(data)

