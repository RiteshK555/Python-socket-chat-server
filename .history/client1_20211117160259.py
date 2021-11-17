import socket
HEADER=64
PORT=5051
SERVER=socket.gethostbyname(socket.gethostname())

client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect((SERVER,PORT))

def msg_from_client1(msg):
    message=msg.encode('utf-8')
    msg_len=len(message)
    send_len=str(msg_len).encode('utf-8')
    send_len+=b' '*(HEADER-len(send_len))
    client1.send(send_len)
    client1.send(message)
print("Welcome to chat server!")
while True:
    a=input()
    msg_from_client1(a)
    if a=="DISCONNECT":
        break
    print(client1.recv(2048).decode('utf-8'))
    msg_rcv=client1.recv(2048).decode('utf-8')
    if len(msg_rcv)>0:
        print(msg_rcv)
    # if msg_rcv:
    #     print(msg_rcv)
    