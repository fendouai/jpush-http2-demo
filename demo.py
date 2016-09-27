import  base64
import json
from hyper import HTTP20Connection
from var_dump import var_dump

conn = HTTP20Connection(host='api.jpush.cn',secure=True)
headers = {}
headers['user-agent'] = 'jpush-api-python-client'
headers['connection'] = 'keep-alive'
headers['content-type'] = 'application/json;charset:utf-8'


username = '6be9204c30b9473e87bad4dc'
password = 'e62664ad421b67270e5c9d5b'

base64string = base64.encodestring(
                '%s:%s' % (username, password))[:-1]
authheader =  "Basic %s" % base64string
#print authheader
headers['Authorization'] =  authheader

body={}
body["platform"]="all"
body["audience"]="all"
notification={}
notification["alert"]="Hi, HTTP/2!"
body["notification"]=notification

conn.connect()
result=conn.request("POST",'/v3/push',headers=headers,body=json.dumps(body))
resp = conn.get_response(result)

#print(resp.read())
print(resp.headers)
headers=resp.headers

