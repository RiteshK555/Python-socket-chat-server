import socket
import threading

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        msg_len=conn.recv(HEADER).decode("utf-8")
        if msg_len:
            msg_len=int(msg_len)
            msg=conn.recv(msg_len).decode("utf-8")
            print(f"{addr}",msg)
            if msg=="DISCONNECT":
                connected=False
                print(f"[{addr}] left the chat.")
            conn.send("msg recieved".encode("utf-8"))
    conn.close()
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] Server started.")
start()