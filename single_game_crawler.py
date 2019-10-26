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

def get_server_task(database,num):
    view_name = '_design/singleplayer_game_add/_view/gameServer'+str(num)
    mapreduce = '''function(doc) {
            if (doc.type === '''+str(num)+'''){
                emit(doc.id, doc.name);
            }
        }'''
    id_list = []

    view_result = database.view(view_name)

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('singleplayer_game_add', 'gameServer'+str(num), mapreduce)
        view.get_doc(database)
        view.sync(database)
        view_result = database.view(view_name)

    for item in view_result:
        game_id = item.key
        if game_id not in id_list:
            id_list.append((game_id, item.value))
    return id_list


def store_game(database,id, name, rate,rate_state,pos,neg,total,au_num,r_num,length,r_length,type):
    item = {
        'id':id,
        'name':name,
        'rate':rate,
        'rate_state':rate_state,
        'image':'https://steamcdn-a.akamaihd.net/steam/apps/'+id+'/capsule_sm_120.jpg',
        'pos':pos,
        'neg':neg,
        'total':total,
        'au_num':au_num,
        'recent_num':r_num,
        'length':length,
        'rlength':r_length,
        'type':type
    }
    database.save(item)



def getgamereviews(game_list,key,type):
    headers = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.232.65:5984/'
    review_db_name = 'test_user'
    server = Server(url % (user, password))
    database1 = server[review_db_name]
    print('Login into couchdb database: ', review_db_name)
    game_db_name = 'test'
    server = Server(url % (user, password))
    database2 = server[game_db_name]
    skip_view = database2.view('_all_docs', include_docs=True)
    skip_list = []
    for i in skip_view:
        if i['doc'].__contains__('id'):
            skip_list.append(i['doc']['id'])
    print('Login into couchdb database: ', game_db_name)
    urltemplate = string.Template(
        'https://store.steampowered.com/appreviews/$id?json=1&language=all&filter=all&review_type=all&purchase_type=all&num_per_page=100&day_range=9223372036854775807&cursor=$cursor')
    endre = re.compile(r'({"success":2})|(no_more_reviews)')
    infore = re.compile(r'{"steamid":"(.*?)","num_games_owned":(\d*),"num_reviews":(\d*),"playtime_forever":(\d*),"playtime_last_two_weeks":(\d*),"last_played":(\d*)}')
    headerre = re.compile(
        r'{"num_reviews":(\d*?),"review_score":(\d*?),"review_score_desc":"(.*?)","total_positive":(\d*?),"total_negative":(\d*?),"total_reviews":(\d*?)}')
    locre = re.compile(r'loccountrycode":"(.*?)"')
    locstatere = re.compile(r'locstatecode":"(.*?)"')
    loccityre = re.compile(r'loccityid":(\d*)')
    cursorre = re.compile(r'"cursor":"(.*?)"')
    for (id, name) in game_list:
        if id in skip_list:
            print('skip---'+str(id)+':'+name)
            continue
        print('start---'+str(id)+':'+name)
        cursor = '*'
        maxError = 10
        errorCount = 0
        count = 0
        au_num=0
        length=0
        r_length=0
        r_num=0
        while True:
            url = urltemplate.substitute({'id': id, 'cursor': urllib.parse.quote(cursor)})
            #print(cursor, url)
            while True:
                try:
                    htmlpage = requests.get(url, timeout=20, headers=headers).text
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
                    try:
                        header_list = headerre.findall(htmlpage)[0]
                    except IndexError:
                        print('except:'+str(id))
                        break
                num = int(header_list[0])
                rate = int(header_list[1])
                rate_state = header_list[2]
                pos_num = int(header_list[3])
                neg_num = int(header_list[4])
                total = int(header_list[5])
                lists = infore.findall(htmlpage)
                if len(lists)==0:
                    break;
                for item in lists:
                    suburl = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='+key+'&steamids=' + \
                             item[0]
                    game_num = int(item[1])
                    review_num = int(item[2])
                    total_time = int(item[3])
                    recent_time = int(item[4])
                    last_played = int(item[5])
                    while True:
                        try:
                            subpage = requests.get(suburl, timeout=20,headers=headers).text
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
                            au_num=au_num+1
                            dict['country']=country
                            dict['steamid']=item[0]
                            dict['game_num']=game_num
                            dict['review_num']=review_num
                            dict['from_game']=id
                            dict['total_time']=total_time
                            dict['recent_time']=recent_time
                            length += total_time
                            r_length += recent_time
                            if r_length>0:
                                r_num=r_num+1
                            dict['last_played'] = last_played
                            dict['type']=type
                            if state != '':
                                dict['state'] = state
                            if city != '':
                                dict['city'] = city
                            database1.save(dict)
            cursor = cursorre.findall(htmlpage)[0]
        store_game(database2, id, name, rate, rate_state, pos_num, neg_num, total, au_num, r_num,length,r_length, type)
        print('end---' + str(id)+':'+name)


def main():
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.232.65:5984/'
    db_name = 'singleplayer_game_add'
    server = Server(url % (user, password))
    if db_name in server:
        database = server[db_name]
        print('Login into couchdb database: ', db_name)
    else:
        database = server.create(db_name)
        print('Create new couchdb database: ', db_name)

    #server_name = sys.argv[1]
    server_name = 'slaver9'

    keys = ['47D02F42306851556CED48DE0BAFC731',
            '2666C7DC59BA3D66C694D350643DF4C3',
            '177A5CAFEDAE3B23DA10115A4C95C9B9',
            'AFD51FA6F2FE61F87BACE4D28391AF04',
            '37314FFEEC79310727026EBF2DB722E8',
            '55DA5B587373A31116CAD4B8B4BE3F05',
            '9E9FA805315870376BABB490E2B92C93',
            'A9F68B7ED431B54E4B1BA8582A29D30B',
            '616CF48C2A8F113FF7C87EB9B0AC8950',
            'A22C81E13075DA81B066A63FFA475674',
            'DA06EC331CB45A13D01C9B83155D4868'

            ]
    if server_name == 'master':
        type=0
        game_list = get_server_task(database,type)
        key = keys[0]
        #print(game_list)
    elif server_name[0:6] == 'slaver':
        type = int(server_name[6:])
        game_list = get_server_task(database,type)
        key = keys[type]
    else:
        print('Server name not found, exit')
        exit(1)

    getgamereviews(game_list,key,type)


if __name__ == '__main__':
    main()
