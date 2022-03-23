"""
Creates a server which sends the compressed python object to the client
"""


import socket
from Message import Message
from compression import *


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

    # pickle the object
    d = jsonpickle.encode(d, unpicklable=True)
    d = d.encode("utf-8")

    # compress the object
    d = compress(d)

    # pickle the datastream
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)
