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


def store_game(database,gameitem):
    if not gameitem.__contains__('country'):
        return
    item = {
        'country':gameitem['country'],
        'steamid': gameitem['steamid'],
        'from_game': gameitem['from_game'],
        'total_time': gameitem['total_time'],
        'recent_time': gameitem['recent_time']
    }
    if gameitem.__contains__('state'):
        item['state'] = gameitem['state']
    if gameitem.__contains__('city'):
        item['city'] = gameitem['city']
    database.save(item)

    # item = {
    #     'id':id,
    #     'name':name,
    #     'rate':rate,
    #     'image':'https://steamcdn-a.akamaihd.net/steam/apps/'+id+'/capsule_sm_120.jpg',
    #     'type':'game'
    # }
    # database.save(item)

def main():
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.232.65:5984/'
    db_name = 'au_user'
    s_name = 'single_game_user'
    m_name = 'multi_game_user'
    server = Server(url % (user, password))
    if db_name in server:
        database1 = server[db_name]
        print('Login into couchdb database: ', db_name)
    else:
        database1 = server.create(db_name)
        print('Create new couchdb database: ', db_name)
    if s_name in server:
        database2 = server[s_name]
        print('Login into couchdb database: ', s_name)
    else:
        database2 = server.create(s_name)
        print('Create new couchdb database: ', s_name)
    if m_name in server:
        database3 = server[m_name]
        print('Login into couchdb database: ', m_name)
    else:
        database3 = server.create(m_name)
        print('Create new couchdb database: ', m_name)
    htmlf = open('singleplayer_game.html', 'r', encoding="utf-8")
    htmlf1 = open('multiplayer_game.html', 'r', encoding="utf-8")
    gameidre = re.compile(r'\/app\/(.*?)\/">')
    htmlpage = htmlf.read()
    if htmlpage is None:
        print('Error')
        sleep(10)
    else:
        pageids = set(gameidre.findall(htmlpage))
    htmlpage1 = htmlf1.read()
    if htmlpage1 is None:
        print('Error')
        sleep(10)
    else:
        pageids1 = set(gameidre.findall(htmlpage1))

    print(pageids)
    print(pageids1)
    all_view = database1.view('_all_docs', include_docs=True)
    skip_list = []
    count=0;
    for i in all_view:
        print(count)
        count=count+1
        if i['doc'].__contains__('from_game'):
            if i['doc']['from_game'] in pageids:
                store_game(database2,i['doc'])
            if i['doc']['from_game'] in pageids1:
                store_game(database3,i['doc'])
    print(len(skip_list))


if __name__ == '__main__':
    main()
