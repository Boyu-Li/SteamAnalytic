#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2018 Andrea Esuli (andrea@esuli.it)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os
import re
import socket
import urllib
import urllib.request
from contextlib import closing
from time import sleep
from couchdb import Server
import json


def download_page(url, timeout, pause):
    htmlpage = None
    while htmlpage is None:
        with closing(urllib.request.urlopen(url, timeout=timeout)) as f:
            htmlpage = f.read()
            sleep(pause)
    return htmlpage

def store_json(dbserver, list):
    index = 0;
    with open("game_detail.json", 'r',encoding='UTF-8') as load_f:

        load_dict = json.load(load_f)
        tmp = load_dict['docs']
    ll = []
    for item in tmp:
        if not item['doc'].__contains__('id'):
            continue
        ll.append(item['doc']['id'])
    print(len(ll))
    count=0
    for item in list:
        obj = {
            'type': index % 10,
            'id': item[0],
            'name': item[1],
            'image': 'https://steamcdn-a.akamaihd.net/steam/apps/' + item[0] + '/capsule_sm_120.jpg'
        }
        if item[0] in ll:
            count = count + 1
            print(item[0]+' is skipped, count:'+str(count))

        dbserver.save(obj)
        print(item[0] + ' is saved')
        index = index + 1


def getgamepages(timeout, maxretries, pause, out):
    # baseurl = 'http://store.steampowered.com/search/results?sort_by=_ASC&snr=1_7_7_230_7&page='
    baseurl = 'singleplayer_game.html'
    htmlf = open('singleplayer_game.html','r',encoding="utf-8")
    htmlf1 = open('multiplayer_game.html', 'r', encoding="utf-8")

    gameidre = re.compile(r'\/app\/(.*?)\/">(.*?)<\/a>')
    pagedir = os.path.join(out, 'singleplayer_games_add')
    if not os.path.exists(pagedir):
        os.makedirs(pagedir)
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
    htmlpage = htmlf.read()
    if htmlpage is None:
        print('Error')
        sleep(pause * 10)
    else:
        pageids = set(gameidre.findall(htmlpage))
    htmlpage1 = htmlf1.read()
    if htmlpage1 is None:
        print('Error')
        sleep(pause * 10)
    else:
        pageids1 = set(gameidre.findall(htmlpage1))

    store_json(database, pageids-pageids1)

def main():
    parser = argparse.ArgumentParser(description='Crawler of Steam game ids and names')
    parser.add_argument('-f', '--force', help='Force download even if already successfully downloaded', required=False,
                        action='store_true')
    parser.add_argument(
        '-t', '--timeout', help='Timeout in seconds for http connections. Default: 180',
        required=False, type=int, default=180)
    parser.add_argument(
        '-r', '--maxretries', help='Max retries to download a file. Default: 5',
        required=False, type=int, default=5)
    parser.add_argument(
        '-p', '--pause', help='Seconds to wait between http requests. Default: 0.5', required=False, default=0.5,
        type=float)
    parser.add_argument(
        '-m', '--maxreviews', help='Maximum number of reviews per item to download. Default:unlimited', required=False,
        type=int, default=-1)
    parser.add_argument(
        '-o', '--out', help='Output base path', required=False, default='data')
    args = parser.parse_args()

    if not os.path.exists(args.out):
        os.makedirs(args.out)

    getgamepages(args.timeout, args.maxretries, args.pause, args.out)


if __name__ == '__main__':
    main()
