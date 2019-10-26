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

def get_state_view(database):
    view_name = '_design/au_user/_view/statemap'

    map_fun = """
                    function(doc) {
                        emit(doc.state, 1);
                    }
                  """
    reduce_fun = "_count"

    id_list = []

    view_result = database.view(view_name)

    try:
        view_result.total_rows

    except:

        view = ViewDefinition('au_user', 'statemap', map_fun, reduce_fun=reduce_fun)
        view.get_doc(database)
        view.sync(database)
        view_result = database.view(view_name)

    for item in view_result:
        print(item)


user = 'user'
password = 'pass'
url = 'http://%s:%s@45.113.232.65:5984/'
db_name = 'au_user'
server = Server(url % (user, password))
if db_name in server:
    database = server[db_name]
    print('Login into couchdb database: ', db_name)
else:
    database = server.create(db_name)
    print('Create new couchdb database: ', db_name)
get_state_view(database)