
import os
import socket , threading
HOST="127.0.0.1"
PORT = 12345
global	a , b , c


def cls():
    	os.system('clear')
            
def listen():
	global sent
	while True:
		data = b""
		while not data:
			data = s.recv(1024)
		print("\b\b\b","\b:", data.decode(), "\n > ", end = "")

def get_input():
	global sent
	while True:
		data = b""
		while not data:
			data = input(" >").encode()
		sent = a.encode(),data

def listen_userID():
	b = s.recv(1024)
	c = s.recv(1024)
	print("Two other users are ready. Presssing enter to continue.")
	cls()

def get_userID():
	print("Enter your User ID:", end = "")
	a = input().encode()
	s.sendall(a)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	cls()
	s.connect((HOST, PORT))

	listen_userID = threading.Thread(target = listen_userID)
	get_userID = threading.Thread(target = get_userID)

	listen_userID.start()
	get_userID.start()
	
	sent = b""



	listen_thread = threading.Thread(target = listen)
	input_thread = threading.Thread(target = get_input)

	listen_thread.start()
	input_thread.start()

	while True:
		if sent:
			s.sendall(sent)
			sent = b""