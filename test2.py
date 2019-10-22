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
# f1=open('game_detail.json','r',encoding='UTF-8')
# f2=open('au_user0.json','r',encoding='UTF-8')
# game=json.load(f1)
# user=json.load(f2)
# list1 = game['docs']
# list2 = user['docs']
# game_list = []
# print("original game count:"+str(len(list1)))
# print('extracting')
#
# for g in list1:
#     if not g['doc'].__contains__('id'):
#         continue
#     if g['doc']['id'] not in game_list:
#         game_list.append(g['doc']['id'])
#
# print('current count:'+str(len(game_list)))
# print()
# print("original user count:"+str(len(list2)))
# s1  = set()
# for a in list2:
#     s1.add(a['doc']['from_game'])
# print('set length:'+str(len(list(s1))))
# print('verifying')
# new_list=[]
# del_list=[]
# for user in list2:
#     if user['doc']['from_game'] in game_list:
#         new_list.append(user)
# for user in list2:
#     if user['doc']['from_game'] not in game_list:
#         del_list.append(user)
# print(len(new_list))
# s2  = set()
# for a in new_list:
#     s2.add(a['doc']['from_game'])
# print('set length:'+str(len(list(s2))))
# pass_list = list(s2)
# f3=open('multiplayer_game0.json','r',encoding='UTF-8')
# mgame=json.load(f3)
# new_mlist = []
# new_mdict = {}
# print(len(mgame['docs']))
# for m in mgame['docs']:
#     if not m['doc'].__contains__('id'):
#         print(m)
#         continue
#     if m['doc']['id'] not in pass_list:
#         new_mlist.append(m)
# new_mdict['docs'] = new_mlist
# with open("multiplayer_game.json","w") as f:
#      json.dump(new_mdict,f)
#      print("加载入文件完成...")

f1=open('multiplayer_game.json','r',encoding='UTF-8')
f2=open('au_user.json','r',encoding='UTF-8')
game=json.load(f1)
user=json.load(f2)
print(len(game['docs']))
print(len(user['docs']))