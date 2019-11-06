import sys
import json
import re
import socket
from couchdb import Server
from couchdb.design import ViewDefinition



def get_server1_task(database):

    id_list = []

    view_result = database.view('_design/game/_view/gameServer1')

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('game', 'gameServer1', '''function(doc) {
            if (doc.type === 0){
                emit(doc.id, doc.name);
            }
        }''')
        view.get_doc(database)
        view.sync(database)
        view_result = database.view('_design/game/_view/gameServer1')

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append(game_id)
    return id_list

def get_server2_task(database):

    id_list = []

    view_result = database.view('_design/game/_view/gameServer2')

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('game', 'gameServer2', '''function(doc) {
            if (doc.type === 1){
                emit(doc.id, doc.name);
            }
        }''')
        view.get_doc(database)
        view.sync(database)
        view_result = database.view('_design/game/_view/gameServer2')

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append(game_id)
    return id_list

def get_server3_task(database):

    id_list = []

    view_result = database.view('_design/game/_view/gameServer3')

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('game', 'gameServer3', '''function(doc) {
            if (doc.type === 2){
                emit(doc.id, doc.name);
            }
        }''')
        view.get_doc(database)
        view.sync(database)
        view_result = database.view('_design/game/_view/gameServer3')

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append(game_id)
    return id_list

def update_name(id):
    baseurl='http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=***&count=3&maxlength=300&format=json'
    baseurl.replace('***',''+id)
    print("crawling--baseurl---")
    gameidre = re.compile(r'')



# Couchdb setup ----------------------------------------------
user = 'user'
password = 'pass'
url = 'http://%s:%s@45.113.234.233:5984/'
db_name = 'game'
server = Server(url % (user, password))
if db_name in server:
    database = server[db_name]
    print('Login into couchdb database: ', db_name)
else:
    database = server.create(db_name)
    print('Create new couchdb database: ', db_name)
# ------------------------------------------------------------
server_name = sys.argv[1]
# server_name = 'slaver2'

if server_name == 'master':
    game_list = get_server1_task(database,0)
    print(game_list)
elif server_name == 'slaver1':
    game_list = get_server2_task(database,1)
    print(game_list)
elif server_name == 'slaver2':
    game_list = get_server3_task(database,2)
    print(game_list)
else:
    print('Server name not found, exit')
    exit(1)

for game in game_list:
    update_name(game)
