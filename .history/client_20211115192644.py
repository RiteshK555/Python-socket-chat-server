import socket
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
