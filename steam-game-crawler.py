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


def download_page(url, timeout, pause):
    htmlpage = None
    while htmlpage is None:
        with closing(urllib.request.urlopen(url, timeout=timeout)) as f:
            htmlpage = f.read()
            sleep(pause)
    return htmlpage

def store_json(dbserver, list):
    index = 0;
    for item in list:
        obj = {
            'type': index % 3+1,
            'id': item[0],
            'name': item[1],
        }
        dbserver.save(obj)
        print(item[0]+' is saved')
        index = index + 1


def getgamepages(timeout, maxretries, pause, out):
    # baseurl = 'http://store.steampowered.com/search/results?sort_by=_ASC&snr=1_7_7_230_7&page='
    baseurl = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    page = 0
    gameidre = re.compile(r'"appid":(.*?),"name":"(.*?)"')
    pagedir = os.path.join(out, 'pages', 'games')
    if not os.path.exists(pagedir):
        os.makedirs(pagedir)
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
    retries = 0
    htmlpage = download_page(baseurl, timeout, pause)
    if htmlpage is None:
        print('Error downloading the URL: ' + url)
        sleep(pause * 10)
    else:
        htmlpage = htmlpage.decode()
        with open(os.path.join(pagedir, 'games-page-%s.html' % page), mode='w', encoding='utf-8') as f:
            f.write(htmlpage)
        pageids = set(gameidre.findall(htmlpage))
        store_json(database, pageids)

    # while True:
    #     url = '%s%s' % (baseurl, page)
    #     print(page, url)
    #     htmlpage = download_page(url, maxretries, timeout, pause)
    #
    #     if htmlpage is None:
    #         print('Error downloading the URL: ' + url)
    #         sleep(pause * 10)
    #     else:
    #         htmlpage = htmlpage.decode()
    #         with open(os.path.join(pagedir, 'games-page-%s.html' % page), mode='w', encoding='utf-8') as f:
    #             f.write(htmlpage)
    #
    #         pageids = set(gameidre.findall(htmlpage))
    #
    #
    #         store_json(database,pageids)
    #         if len(pageids) == 0:
    #             # sometimes you get an empty page but it is not actually
    #             # the last one, so it is better to retry a few times before
    #             # considering the work done
    #             if retries < maxretries:
    #                 print('empty page', retries)
    #                 sleep(5)
    #                 retries += 1
    #                 continue
    #             else:
    #                 break
    #         print(len(pageids), pageids)
    #         retries = 0
    #         page += 1


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