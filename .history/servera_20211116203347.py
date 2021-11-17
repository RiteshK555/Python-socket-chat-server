import selectors
import socket
sel=selectors.DefaultSelector()
host=''
lsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind(())