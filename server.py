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
  while True:
    print(data_in)
    data_in = []
    for thread in threads:
      data_out.append((thread, thread))

def thread(client): #threads a client
  threads.append(client.fileno())
  print(threads)
  while True:
    try:
      data = client.recv(1024)
      data_in.append((client.fileno(), data))
      for data in data_out:
        if data[0] == client.fileno(): #tests for specified client
          client.send(bytes(data[1], 'utf-8')) #sends data
          print("sending data")
          data_out.remove(data)
    except:
      break
  print("removing thread to client "+str(client))
  try:
    threads.remove(client.fileno())
  except:
    pass
  client.close()

Thread(target = game).start() #starts the main game loop for it to not be stopped by socket.accept()

while True:
  client, address = socket.accept() #accepts the client; WARNING: blocks the entire un-threaded program until a client attempts a connection
  Thread(target = thread, args = (client, )).start()
  print("accepted new client"+str(client)+str(address))

  data_in = []

socket.close()
