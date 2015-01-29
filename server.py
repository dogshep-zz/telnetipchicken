import socket
import sys
from thread import *
import pygeoip

HOST = ''
PORT = 8888

gi = pygeoip.GeoIP('GeoIP.dat')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '[INFO] Socket Created'

#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print '[ERROR] Bind failed. Error code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

print '[INFO] Socket bind complete'

#Start listening on socket
s.listen(10)
print '[INFO] Socket now listening'

#Function for talking

def clientthread(conn,addr):
	#Send message
#	conn.send('Welcome to the server. Type something and hit enter\n')
	conn.send('You are connected from: ' + str(addr) + ' from' + gi.country_name_by_addr(addr[0]) + '\n')
	conn.send('Hit enter to leave...')
#	while True:
	data = conn.recv(1024)
	conn.close()

# keep talking with client
while 1:
	#wait for connection
	conn, addr = s.accept()
	print '[INFO] Connected with ' + addr[0] + ':' + str(addr[1]) + ' from' + gi.country_name_by_addr(addr[0])
	#start chatting
	start_new_thread(clientthread ,(conn,addr,))
	
s.close()
