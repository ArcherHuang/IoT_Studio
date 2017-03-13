import time
import datetime
import sys  
import httplib, urllib
import json

def post_to_alliotcloud(payload):
    headers = {"Content-type": "application/json",}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("192.168.43.130:1880")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/v1/temperature", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    t0 = "26"
    t = time.time();
    date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
    payload = {"date":date ,"temperature":t0}
    post_to_alliotcloud(payload)
    time.sleep(10)