import socket
from compression import *


HEADERSIZE = 10

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:

    full_msg = b''
    new_msg = True
    while True:
        msg = ClientMultiSocket.recv(2048)
        if new_msg:
            print("new msg len:", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg received")
            print(full_msg[HEADERSIZE:])

            # unpickle the data stream
            data = pickle.loads(full_msg[HEADERSIZE:])

            # decompress the object
            data = decompress(data)

            # unpickle the object
            data = data.decode("utf-8")
            data = jsonpickle.decode(data)
            print(data.data)
            new_msg = True
            full_msg = b""
ClientMultiSocket.close()