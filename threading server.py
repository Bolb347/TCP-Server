import socket, threading, types

host = "127.0.0.1"
port = 4096

socket = socket.socket()
socket.bind((host, port))
socket.listen()

data_out = []

threads = []

def addData(data_list, data, client_file_descriptor):
  data_list.append(types.SimpleNamespace(data, client_file_descriptor))

def thread(client): #threads a client
  print("initializing threading")
  threads.append(client.fileno())
  while True:
    try:
      data = client.recv(1024) #recieves 1024 bytes of data from the given client
      if data == None: #removes the client if it has disconnected
        print("removing thread to client "+str(client))
        break

      data = b"hello" #creates data (needs to be tested for on client side)
      client.send(data) #sends the data
      print("sent data: "+str(data))
    except:
      break
  try:
    threads.remove(client.fileno())
  client.close()

while True:
  client, address = socket.accept() #accepts the client
  print("accepted new client"+str(client)+str(address))

  threading._start_new_thread(thread, (client,)) #creates the thread

socket.close()
