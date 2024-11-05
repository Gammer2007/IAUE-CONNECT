# Fuzzer program

import socket


while True:
	try:
		buffer = 'A'*100
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.create_connection(('192.168.91.1','8000'))
		s.send('python '+buffer)
		s.close()
		sleep(1)
		buffer += 'A'*100
	except ConnectionError:
		print(f" Creshed at {buffer}")
		sys.exit()