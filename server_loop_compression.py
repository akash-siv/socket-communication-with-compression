import socket
import os
from _thread import *
from Message import Message
from compression import *
import time

HEADERSIZE = 10

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
data = {"trans":"5 nos",
        "vali":"akash",
        "hash":"0x154ac"}
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    # connection.send(str.encode('Server is working:'))
    while True:
        d = Message('socketConnector', 'PoolTrue', data)

        # pickle the object
        d = jsonpickle.encode(d, unpicklable=True)
        d = d.encode("utf-8")

        # compress the object
        d = compress(d)
        # pickle the datastream
        msg = pickle.dumps(d)

        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
        connection.send(msg)
        time.sleep(1)
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()