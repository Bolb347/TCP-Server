import socket, threading

lock = threading.Lock()

host = "127.0.0.1"
port = 4096

socket = socket.socket()
socket.bind((host, port))
socket.listen()

def thread(client): #threads a client
  print("initializing threading")
  while True:
    try:
      data = client.recv(1024) #recieves 1024 bytes of data from the given client
      if data == None: #removes the client if it has disconnected
        print("removing thread to client "+str(client))
        lock.release() #removes the client from threading
        break

      data = b"hello" #creates data (needs to be tested for on client side)
      client.send(data) #sends the data
      print("sent data: "+str(data))
    except:
      print("ERR")
  client.close()
  lock.release()

while True:
  client, address = socket.accept() #accepts the client
  print("accepted new client"+str(client)+str(address))
  lock.acquire()

  threading._start_new_thread(thread, (client,)) #creates the thread

socket.close()
