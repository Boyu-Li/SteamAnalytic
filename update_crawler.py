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
import csv
import os
import re
import socket
import string
import urllib
import urllib.request
from contextlib import closing
from time import sleep
import requests

def download_page(url, maxretries, timeout, pause):
    tries = 0
    htmlpage = None
    while tries < maxretries and htmlpage is None:
        try:
            with closing(urllib.request.urlopen(url, timeout=timeout)) as f:
                htmlpage = f.read()
                sleep(pause)
        except (urllib.error.URLError, socket.timeout, socket.error):
            tries += 1
    return htmlpage


def getgameids(filename):
    ids = set()
    with open(filename, encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            dir = row[0]
            id_ = row[1]
            name = row[2]
            ids.add((dir, id_, name))
    return ids


def getgamereviews(timeout, maxretries, pause, out):
    urltemplate = string.Template(
        'https://store.steampowered.com/appreviews/$id?json=1&language=all&filter=all&review_type=all&purchase_type=all&num_per_page=100&day_range=9223372036854775807&cursor=$cursor')
        #'http://store.steampowered.com//appreviews/$id?start_offset=$offset&filter=recent&language=english')
    endre = re.compile(r'({"success":2})|(no_more_reviews)')
    infore = re.compile(r'"recommendationid":"(.*?)"')
    headerre = re.compile(r'{"num_reviews":(\d*?),"review_score":(\d*?),"review_score_desc":"(.*?)","total_positive":(\d*?),"total_negative":(\d*?),"total_reviews":(\d*?)}')

    cursorre = re.compile(r'"cursor":"(.*?)"')
    ids = [('a','301980','*')]
    for (dir, id_, cursor) in ids:
        if dir == 'sub':
            print('skipping sub %s %s' % (id_, cursor))
            continue

        # gamedir = os.path.join(out, 'pages', 'reviews', '-'.join((dir, id_)))
        #
        # donefilename = os.path.join(gamedir, 'reviews-done.txt')
        # if not os.path.exists(gamedir):
        #     os.makedirs(gamedir)
        # elif os.path.exists(donefilename):
        #     print('skipping app %s %s' % (id_, name))
        #     continue

        print(dir, id_, cursor)

        cursor = '*'
        maxError = 10
        errorCount = 0
        count = 0
        total = 0
        res = []
        cursor_lists = []
        while True:
            url = urltemplate.substitute({'id': id_, 'cursor': urllib.parse.quote(cursor)})

            print(cursor, url)
            htmlpage = requests.get(url).text
            lists = []

            if htmlpage is None:
                print('Error downloading the URL: ' + url)
                sleep(pause * 3)
                errorCount += 1
                if errorCount >= maxError:
                    print('Max error!')
                    break
            else:
                if endre.search(htmlpage):
                    break
                if cursor == '*':
                    header_list = headerre.findall(htmlpage)
                    print(total)
                lists = infore.findall(htmlpage)
                for item in lists:
                    if item not in res:
                        print(item)
                        res.append(item)
                print(len(res))
                cursor = cursorre.findall(htmlpage)[0]
                if cursor in cursor_lists or len(res) == total:
                    print(len(res))
                    break
                else:
                    cursor_lists.append(cursor)
        print(len(res))


def main():
    parser = argparse.ArgumentParser(description='Crawler of Steam reviews')
    parser.add_argument('-f', '--force', help='Force download even if already successfully downloaded', required=False,
                        action='store_true')
    parser.add_argument(
        '-t', '--timeout', help='Timeout in seconds for http connections. Default: 180',
        required=False, type=int, default=180)
    parser.add_argument(
        '-r', '--maxretries', help='Max retries to download a file. Default: 5',
        required=False, type=int, default=3)
    parser.add_argument(
        '-p', '--pause', help='Seconds to wait between http requests. Default: 0.5', required=False, default=0.5,
        type=float)
    parser.add_argument(
        '-m', '--maxreviews', help='Maximum number of reviews per item to download. Default:unlimited', required=False,
        type=int, default=-1)
    parser.add_argument(
        '-o', '--out', help='Output base path', required=False, default='data')
    parser.add_argument(
        '-i', '--ids', help='File with game ids', required=False, default='./data/games.csv')
    args = parser.parse_args()

    if not os.path.exists(args.out):
        os.makedirs(args.out)

    # ids = getgameids(args.ids)
    #
    # print('%s games' % len(ids))

    getgamereviews(args.timeout, args.maxretries, args.pause, args.out)


if __name__ == '__main__':
    main()
