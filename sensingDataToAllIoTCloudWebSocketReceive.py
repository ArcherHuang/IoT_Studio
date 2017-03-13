import websocket

websocket.enableTrace(True)
ws = websocket.create_connection("ws://192.168.43.130:1880/ws/temperature/view")

while True:
	result = ws.recv()
	print "Received '%s'" % result