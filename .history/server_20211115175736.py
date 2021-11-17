import socket
import threading

PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
# print(socket.gethostbyname(socket.gethostname()))
# print(socket.gethostname())
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
