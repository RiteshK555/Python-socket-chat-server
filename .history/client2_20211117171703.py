import socket
import threading
HEADER=64
PORT=5051
SERVER=socket.gethostbyname(socket.gethostname())

client2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client2.connect((SERVER,PORT))

def msg_from_client1(msg):
    message=msg.encode('utf-8')
    msg_len=len(message)
    send_len=str(msg_len).encode('utf-8')
    send_len+=b' '*(HEADER-len(send_len))
    client2.send(send_len)
    client2.send(message)
print("Welcome to chat server!")
def handle_input():
    while True:
        a=input()
        msg_from_client1(a)
        if a=="DISCONNECT":
            break
    #kill thread
    client2.close()

def handle_recieve():
    while True:
        msg_rcv=client2.recv(2048).decode('utf-8')
        if len(msg_rcv)>0 and msg_rcv!=:
            print(msg_rcv)
    

thread=threading.Thread(target=handle_input,args=())
thread.start()
thread2=threading.Thread(target=handle_recieve,args=())
thread2.start()
    