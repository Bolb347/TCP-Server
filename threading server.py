import socket, threading

lock = threading.lock()

host = "127.0.0.1"
port = 2048

socket = socket.socket()
socket.bind((host, port))
socket.listen()

def thread(client): #threads a client
  while True:
    data = client.recv(1024) #recieves 1024 bytes of data from the given client
    if data is None: #removes the client if it has disconnected
      print("removing thread to client "+client)
      lock.release() #removes the client from threading
      break

    data = b"hello" #creates data (needs to be tested for on client side)
    client.send(data) #sends the data
  client.close()

while True:
  client, address = socket.accept() #accepts the client
  lock.acquire()

  start_new_thread(thread, (client,)) #creates the thread

socket.close()
