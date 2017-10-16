#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import IP_name

SER_HOST = socket.gethostbyname(socket.gethostname())
SER_PORT = 10050
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SER_HOST, SER_PORT))
local_host, local_port  = s.getsockname()
peer_host, peer_port = s.getpeername()

if (local_host, local_port) == (SER_HOST, SER_PORT):	
	local_name = 'Server'
else:
	local_name = IP_name.names.get(local_host, 'Unkown')
if (peer_host, peer_port) == (SER_HOST, SER_PORT):	
	peer_name = 'Server'
else:
	peer_name = IP_name.names.get(peer_host, 'Unkown')
print 'Connected to: %s(%s:%s)'%(peer_name, peer_host, peer_port)

while True:
	while True:
		print '%s\t:'%local_name,
		msg = raw_input()
		if msg: break
	s.sendall(msg)
	if msg == 'exit': break
	reply = s.recv(1024)
	if reply == 'exit': break
	print '%s\t: %s'%(peer_name, reply)

print 'Disconnected from: %s(%s:%s)'%(peer_name, peer_host, peer_port)
