import selectors
import socket
sel=selectors.DefaultSelector()
host='127.0.0.1'
port=8080
lsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()
print('Listening on',(host,port))
lsock.setblocking(False)
sel.