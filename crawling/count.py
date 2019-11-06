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



def getgamereviews():
    headers = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    user = 'user'
    password = 'pass'
    url = 'http://%s:%s@45.113.232.65:5984/'
    review_db_name = 'test'
    server = Server(url % (user, password))
    database1 = server[review_db_name]
    print('Login into couchdb database: ', review_db_name)
    game_db_name = 'game_detail'
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
    rev_count = 0
    game_count=0
    for id in skip_list:

        cursor = '*'
        maxError = 10
        errorCount = 0
        count = 0
        au_num=0
        length=0
        r_length=0
        r_num=0

        url = urltemplate.substitute({'id': id, 'cursor': urllib.parse.quote(cursor)})
        # print(cursor, url)
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
                print('end---' + str(id) +'   0')
                game_count = game_count + 1
                continue
            try:
                header_list = headerre.findall(htmlpage)[0]
            except IndexError:
                print('end---' + str(id) + '   0')
                game_count = game_count + 1
                continue
            total = int(header_list[5])
            rev_count=rev_count+total
            game_count=game_count+1

        # store_game(database2, id, name, rate, rate_state, pos_num, neg_num, total, au_num, r_num,length,r_length, type)
        print('end---' + str(id) + '   '+str(game_count)+'   '+str(rev_count))


def main():

    getgamereviews()


if __name__ == '__main__':
    main()
