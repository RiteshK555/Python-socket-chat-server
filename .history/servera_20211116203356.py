import selectors
import socket
sel=selectors.DefaultSelector()
host='127.0.0.1'
port=
lsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind(())