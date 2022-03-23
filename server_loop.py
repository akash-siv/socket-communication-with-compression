"""
server for sending python object in socket communication in loop.
only for testing purpose.
"""

import socket
import time
import pickle
from Message import Message


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)
data = {"trans":"5 nos",
        "vali":"akash",
        "hash":"0x154ac"}

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = Message('socketConnector', 'PoolTrue', data)
    while True:
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        print(msg)
        clientsocket.send(msg)
        time.sleep(1)