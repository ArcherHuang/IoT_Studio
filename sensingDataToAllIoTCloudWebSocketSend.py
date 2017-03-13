import time
import sys  
import websocket
import datetime


websocket.enableTrace(True)
ws = websocket.create_connection("ws://192.168.43.130:1880/ws/temperature/receive")

while True:
	t0 = "28"
	print "Temp: " + t0
	
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	vals = "{\"date\" : \"" + date + "\", \"temperature\":" + t0 + "}"
	time.sleep(1);
	ws.send(vals);
	print vals;