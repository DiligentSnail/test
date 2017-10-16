#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import IP_name

HOST = ''
PORT = 10050
local_name = 'Server'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

print 'Waiting clients to connect...'
conn, addr = s.accept()
client = IP_name.names.get(addr[0], 'Unkown')

print 'Connected by client: %s(%s:%s)'%(client, addr[0], addr[1])

while True:
	msg = conn.recv(1024)
	if msg == 'exit': break
	print '%s\t: %s '%(client, msg)
	while True:
		print '%s\t:'%(local_name),
		reply = raw_input()
		if reply: break
	conn.sendall(reply)
	if reply == 'exit': break

print 'Disconnected from client: %s(%s:%s)'%(client, addr[0], addr[1])
conn.close()
