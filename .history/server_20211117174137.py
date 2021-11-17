import socket
import threading

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))
arr=[]
trds=[]
def handle_client(conn,addr):
    print(f"{addr} joined the chat.")
    for e in arr:
        if e!=conn:
            e.send("addr}: {msg}".encode("utf-8"))
    connected=True
    while connected:
        msg_len=conn.recv(HEADER).decode("utf-8")
        if msg_len:
            msg_len=int(msg_len)
            msg=conn.recv(msg_len).decode("utf-8")
            if msg=="DISCONNECT":
                connected=False
                print(f"[{addr}] left the chat.")
                conn.close()
                arr.remove(conn)
            else:
                print(f"{addr}:",msg)
                for e in arr:
                    if e!=conn:
                        e.send(f"{addr}: {msg}".encode("utf-8"))
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        arr.append(conn)

print("[STARTING] Server started.")
start()

