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

def get_server1_task(database):

    id_list = []

    view_result = database.view('_design/multiplayer_game/_view/gameServer1')

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('multiplayer_game', 'gameServer1', '''function(doc) {
            if (doc.type === 1){
                emit(doc.id, doc.name);
            }
        }''')
        view.get_doc(database)
        view.sync(database)
        view_result = database.view('_design/multiplayer_game/_view/gameServer1')

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append((game_id, item.value))
    return id_list

def get_server2_task(database):

    id_list = []

    view_result = database.view('_design/multiplayer_game/_view/gameServer2')

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('multiplayer_game', 'gameServer2', '''function(doc) {
            if (doc.type === 2){
                emit(doc.id, doc.name);
            }
        }''')
        view.get_doc(database)
        view.sync(database)
        view_result = database.view('_design/multiplayer_game/_view/gameServer2')

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append((game_id, item.value))
    return id_list

def get_server3_task(database):

    id_list = []

    view_result = database.view('_design/multiplayer_game/_view/gameServer3')

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('multiplayer_game', 'gameServer3', '''function(doc) {
            if (doc.type === 3){
                emit(doc.id, doc.name);
            }
        }''')
        view.get_doc(database)
        view.sync(database)
        view_result = database.view('_design/multiplayer_game/_view/gameServer3')

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append((game_id, item.value))
    return id_list

def store_game(database,id, name, rate):
    item = {
        'id':id,
        'name':name,
        'rate':rate,
        'image':'https://steamcdn-a.akamaihd.net/steam/apps/'+id+'/capsule_sm_120.jpg',
        'type':'game'
    }
    database.save(item)



def getgamereviews(game_list,key):
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.234.233:5984/'
    db_name = 'game_detail'
    server = Server(url % (user, password))
    if db_name in server:
        database = server[db_name]
        print('Login into couchdb database: ', db_name)
    else:
        database = server.create(db_name)
        print('Create new couchdb database: ', db_name)

    urltemplate = string.Template(
        'https://store.steampowered.com/appreviews/$id?json=1&language=all&filter=all&review_type=all&purchase_type=all&num_per_page=100&day_range=9223372036854775807&cursor=$cursor')
    endre = re.compile(r'({"success":2})|(no_more_reviews)')
    infore = re.compile(r'"steamid":"(.*?)".*?"playtime_forever":(\d*)')
    headerre = re.compile(
        r'{"num_reviews":(\d*?),"review_score":(\d*?),"review_score_desc":"(.*?)","total_positive":(\d*?),"total_negative":(\d*?),"total_reviews":(\d*?)}')
    locre = re.compile(r'loccountrycode":"(.*?)"')
    locstatere = re.compile(r'locstatecode":"(.*?)"')
    loccityre = re.compile(r'loccityid":(\d*)')
    cursorre = re.compile(r'"cursor":"(.*?)"')
    for (id, name) in game_list:
        cursor = '*'
        maxError = 10
        errorCount = 0
        count = 0
        while True:
            url = urltemplate.substitute({'id': id, 'cursor': urllib.parse.quote(cursor)})

            #print(cursor, url)
            htmlpage = requests.get(url).text

            if htmlpage is None:
                print('Error downloading the URL: ' + url)
                sleep(5)
                errorCount += 1
                if errorCount >= maxError:
                    print('Max error!')
                    break
            else:
                if endre.search(htmlpage):
                    break
                if cursor == '*':
                    header_list = headerre.findall(htmlpage)[0]
                num = int(header_list[0])
                rate = int(header_list[1])
                total = int(header_list[5])
                lists = infore.findall(htmlpage)

                count+=num
                for item in lists:
                    suburl = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=646968A1C8E1AF8E602F1E1193F07C1E&steamids=' + \
                             item[0]

                    while True:
                        try:
                            subpage = requests.get(suburl, timeout=20).text
                            break
                        except requests.exceptions.ConnectionError:
                            print('ConnectionError -- please wait 3 seconds')
                            time.sleep(3)
                        except requests.exceptions.ChunkedEncodingError:
                            print('ChunkedEncodingError -- please wait 3 seconds')
                            time.sleep(3)
                        except:
                            print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
                            time.sleep(3)
                    if subpage is not None:
                        country=''
                        state=''
                        city=''
                        dict={}
                        try:
                            country = locre.findall(subpage)[0]
                            #print(country)
                            state = locstatere.findall(subpage)[0]
                            #print(state)
                            city = loccityre.findall(subpage)[0]
                            #print(city)
                        except IndexError:
                            pass
                        if country=='AU':
                            dict['country']=country
                            dict['steamid']=id
                            dict['type']='user'
                            if state != '':
                                dict['state'] = state
                            if city != '':
                                dict['city'] = city
                            database.save(dict)
                cursor = cursorre.findall(htmlpage)[0]
                if count >= total:
                    break
        store_game(database, id, name, rate)


def main():
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.234.233:5984/'
    db_name = 'multiplayer_game'
    server = Server(url % (user, password))
    if db_name in server:
        database = server[db_name]
        print('Login into couchdb database: ', db_name)
    else:
        database = server.create(db_name)
        print('Create new couchdb database: ', db_name)

    server_name = sys.argv[1]
    #server_name = 'master'

    keys = ['47D02F42306851556CED48DE0BAFC731',
            '2666C7DC59BA3D66C694D350643DF4C3',
            '177A5CAFEDAE3B23DA10115A4C95C9B9',
            'AFD51FA6F2FE61F87BACE4D28391AF04'
            ]
    if server_name == 'master':
        game_list = get_server1_task(database)
        key = keys[0]
    elif server_name == 'slaver1':
        game_list = get_server2_task(database)
        key = keys[1]
    elif server_name == 'slaver2':
        game_list = get_server3_task(database)
        key = keys[2]
    else:
        print('Server name not found, exit')
        exit(1)

    getgamereviews(game_list,key)


if __name__ == '__main__':
    main()
