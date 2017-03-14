# **************************************************************************************************************************
# Version:     2017.1.12 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + WebSocket
# **************************************************************************************************************************
#  
# 1. install wget
#    opkg update
#    opkg install wget
#
# 2. install setuptools
#	 curl https://bootstrap.pypa.io/ez_setup.py -k -o - | python
#
# 3. install six
# 	 wget --no-check-certificate https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz
# 	 tar zxvf six-1.10.0.tar.gz
#	 cd six-1.10.0
#	 python setup.py install
#
# 4. install Websocket
#	 wget --no-check-certificate https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz
#	 tar zxvf websocket_client-0.32.0.tar.gz
#	 cd websocket_client-0.32.0
#	 python setup.py install
# 
# **************************************************************************************************************************

import time
import sys  
import websocket
import datetime

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

websocket.enableTrace(True)
ws = websocket.create_connection("ws://192.168.43.219:1880/ws/temperature/receive")

while True:
	h0 = value.get("Humidity")
	t0 = value.get("Temperature")
	
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	vals = "{\"date\" : \"" + date + "\", \"temperature\":" + t0 + "\", \"humidity\":" + h0 + "}"
	print vals;
	ws.send(vals)
	time.sleep(1)
