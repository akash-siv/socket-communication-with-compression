"""
socket client which receives compressed object from server and extract it.
if the buffer is small it loops until it receives all the packets and extracts the objects.
"""

import socket
from compression import *

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(2048)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
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
