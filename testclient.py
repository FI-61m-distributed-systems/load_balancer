'''Python 2.7.3.'''

# @polyvika

import urllib
import urllib2
import json

url = 'http://localhost:8001'
## type of requsts
hru={
    "type": "get",
    "fields":
    [
       "email",
       "money","password","game"
    ],
    "conditions":
    [
       ["user", "=", "vika"]
    ]
}
tr={
    "type": "update",
    "transaction":
    [
        {
          "action": "update",
          "field": "password",
          "value": "bub",
          "conditions": [["user", "=", "10"]]
       },

     {
          "action": "delete",
          "conditions": [["user", "=", "rrrrrrrr"]]
       },
        {
          "action": "insert",
          "user": "d",
          "password": "money",
          "email": "vkdjs",

       }

    ]
 }

param=urllib.urlencode({'json': json.dumps(tr)})
response = urllib2.urlopen(url,param)
print response.getcode()
print response.headers['Content']
response.close()