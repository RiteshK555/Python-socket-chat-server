import socket
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect((SERVER,PORT))

def msg_from_client1(msg):
    client1.send(msg.encode())
    msg=client1.recv(2048).decode()