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
        return a

def handle_recieve():
    while True:
    def handle_input():
        a=input()
    msg_from_client1(a)
    return a

print("Welcome to chat server!")

def handle_recieve():
    msg_rcv=client1.recv(2048).decode('utf-8')
    print(msg_rcv)
    if len(msg_rcv)>0:
        print("hello")
        print(msg_rcv)
    
while True:
    thread=threading.Thread(target=handle_input,args=())
    thread.start()
    thread2=threading.Thread(target=handle_recieve,args=())
    thread2.start()
    
while True:
    thread=threading.Thread(target=handle_input,args=())
    thread.start()
    thread2=threading.Thread(target=handle_recieve,args=())
    thread2.start()
# while True:
#     a=input()
#     msg_from_client1(a)
#     if a=="DISCONNECT":
#         break
#     print("first")
#     msg_rcv=client2.recv(2048).decode('utf-8')
#     print("second")
#     print(msg_rcv)
#     if len(msg_rcv)>0:
#         print("hello")
#         print(msg_rcv)
    # msg_rcv=client2.recv(2048).decode('utf-8')
    # if msg_rcv:
    #     print(msg_rcv)

    