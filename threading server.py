import socket, threading

host = "127.0.0.1"
port = 52000

socket = socket.socket()
socket.bind((host, port))
socket.listen()

data_out = []
data_in = []

threads = []

def thread(client): #threads a client
  threads.append(client.fileno())
  print(threads)
  while True:
    try:
      data = client.recv(1024)
      data_in.append((client.fileno(), data))
      if data == None: #removes the client if it has disconnected
        break
      for data in data_out:
        if data[0] == client.fileno(): #tests for specified client
          client.send(bytes(data[1], 'utf-8')) #sends data
          print("sending data")
    except:
      break
  print("removing thread to client "+str(client))
  try:
    threads.remove(client.fileno())
  finally:
    pass
  client.close()

while True:  
  client, address = socket.accept() #accepts the client
  print("accepted new client"+str(client)+str(address))

  print("checking for threads")
  threading._start_new_thread(thread, (client, )) #creates the thread with (function, arguments)
  print("adding threads")


  if len(threads):
    data_out.append((threads[0], "hi"))
  
  #data_out = []
  data_in = []

socket.close()
