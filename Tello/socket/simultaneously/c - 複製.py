



import os
import socket , threading
HOST="127.0.0.1"
PORT = 12345
global	b
global	a


def cls():
    	os.system('clear')
            
def listen():
	global sent
	while True:
		data = b""
		while not data:
			data = s.recv(1024)
		print("\b",b.decode(),": ", data.decode(), "\n > ", end = "")

def get_input():
	global sent
	while True:
		data = b""
		while not data:
			data = input(" >").encode()
		sent = data



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	cls()
	print("Enter your User ID:")
	a=input().encode()
	s.connect((HOST, PORT))
	sent = b""

	s.sendall(a)
	print("Waiting for another User log in.")
	b = s.recv(1024)
	print("Connecting with ",b.decode())

	listen_thread = threading.Thread(target = listen)
	input_thread = threading.Thread(target = get_input)

	listen_thread.start()
	input_thread.start()

	while True:
		if sent:
			s.sendall(sent)
			sent = b""