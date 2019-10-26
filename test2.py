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
db_name = 'game_detail'
server = Server(url % (user, password))
if db_name in server:
    database = server[db_name]
    print('Login into couchdb database: ', db_name)
else:
    database = server.create(db_name)
    print('Create new couchdb database: ', db_name)

f1=open('game_detail.json','r',encoding='UTF-8')
game=json.load(f1)['docs']
for i in game:
    print(i)
    if not i['doc'].__contains__('id'):
        continue
    data={
        'id':i['doc']['id'],
        'name':i['doc']['name'],
        'rate':i['doc']['rate'],
        'rate_state':i['doc']['rate_state'],
        'image':i['doc']['image'],
        'pos':i['doc']['pos'],
        'neg':i['doc']['neg'],
        'total':i['doc']['total'],
        'au_num':i['doc']['au_num'],
        'recent_num':i['doc']['recent_num'],
        'length':i['doc']['length'],
        'rlength':i['doc']['rlength'],
        'type':i['doc']['type']
    }
    print(data)
    database.save(data)

