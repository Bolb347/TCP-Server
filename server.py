import socket
from threading import Thread

host = "127.0.0.1"
port = 52000

socket = socket.socket()
socket.bind((host, port))
socket.listen()

data_out = []
data_in = []

threads = []

def game():
    global data_in, data_out, threads
    while True:
        data_in = []
        for thread in threads:
            for i in range(5):
                data_out.append((thread, str(i).encode('utf-8')))

def thread(client): #threads a client
    global data_in, data_out, threads
    threads.append(client.fileno())
    print(threads)
    data = None
    try:
        data = client.recv(1024)
    except:
        print("encountered err while recv")
    
    data_in.append((client.fileno(), data))
    for data in data_out:
        if data[0] == client.fileno(): #tests for specified client
            try:
                client.send(data[1]) #sends data
            except:
                print("encountered err while sending")
            break
        data_out.remove(data)
        print("removing thread to client "+str(client))
    try:
        threads.remove(client.fileno())
    except:
        pass
    
    client.close()

Thread(target = game).start() #starts the main game loop for it to not be stopped by socket.accept()

while True:
    print("accepting...") 
    client, address = socket.accept() #accepts the client; WARNING: blocks the entire un-threaded program until a client attempts a connection
    Thread(target = thread, args = (client, )).start()
    print("accepted new client"+str(client)+str(address))

    data_in = []

socket.close()
