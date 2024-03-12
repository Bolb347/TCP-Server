import socket, time
from threading import Thread

host = "127.0.0.1"
port = 52000

socket = socket.socket()
socket.bind((host, port))
socket.listen()

data_out = []
data_in = []

threads = []

def main():
    global data_in, data_out, threads
    while True:
        time.sleep(1)
        for data in data_in:
            print(data[0])
        data_in = []
        for thread in threads:
            data_out.append((thread, str(1).encode('utf-8')))

def thread(client): #threads a client
    global data_in, data_out, threads
    broken = False
    threads.append(client.fileno())
    print(threads)
    while not broken:
        data = None
        try:
            data = client.recv(1024).decode('utf-8')
        except:
            print("encountered err while recv")
        
        data_in.append((client.fileno(), data))
        for data in data_out:
            if data[0] == client.fileno(): #tests for specified client
                try:
                    client.send(data[1]) #sends data
                except:
                    print("encountered err while sending")
                    broken = True
                data_out.remove(data)
                break
    
    print("removing thread to client "+str(client))
    try:
        threads.remove(client.fileno())
    except:
        pass
    
    client.close()

Thread(target = main).start() #starts the main game loop for it to not be stopped by socket.accept()

while True:
    print("accepting...") 
    client, address = socket.accept() #accepts the client; WARNING: blocks the entire un-threaded program until a client attempts a connection
    Thread(target = thread, args = (client, )).start()
    print("accepted new client"+str(client)+str(address))

socket.close()
