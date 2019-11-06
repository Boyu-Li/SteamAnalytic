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
url = 'https://store.steampowered.com/appreviews/259381?json=1&language=all&filter=all&review_type=all&purchase_type=all&num_per_page=100&day_range=9223372036854775807&cursor=*'
print()
htmlpage = requests.get(url).text
key = 'DA06EC331CB45A13D01C9B83155D4868'
if True:
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.232.65:5984/'
    review_db_name = 'test_user'
    server = Server(url % (user, password))
    database1 = server[review_db_name]
    print('Login into couchdb database: ', review_db_name)
    game_db_name = 'game_detail'
    server = Server(url % (user, password))
    database2 = server[game_db_name]
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
    name = 'test'
    type = '99'
    id = 300080
    for i in range(1):
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
                    htmlpage = requests.get(url, timeout=20).text
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
                    header_list = headerre.findall(htmlpage)[0]
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
        print(id)
        print('end---' + str(id)+':'+name)
