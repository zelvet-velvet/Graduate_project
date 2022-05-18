import socket
UDP_IP = '127.168.0.101'
UDP_PORT = 8889
BUFFER_SIZE = 1024
MESSAGE = b"command"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((UDP_IP, UDP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print ("received data:", data)