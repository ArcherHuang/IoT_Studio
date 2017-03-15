# *************************************************************************
# Version:     2016.03.14
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + IoT Studio
# *************************************************************************
# 
# 1. update opkg & install wget & disable bridge
#    opkg update
#    uci set yunbridge.config.disabled=0
#    uci commit
#    reboot
#
# *************************************************************************

import time
import datetime
import sys  
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

def post_to_alliotcloud(payload):
    headers = {"Content-type": "application/json",}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("192.168.43.219:1880")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/v1/temperatureHumidity", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    h0 = value.get("Humidity")
    t0 = value.get("Temperature")
    t = time.time();
    date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
    payload = {"date":date , "temperature":t0, "humidity":h0}
    post_to_alliotcloud(payload)
    time.sleep(10)