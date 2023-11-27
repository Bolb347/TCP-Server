import socket, selectors, types

selector = selectors.DefaultSelector()

host = "127.0.0.1" #set to the host of the server's ip
port = 4096 #set to the port to listen to (needs to be larger than 1024)

socket = socket.socket()
socket.bind((host, port))
socket.listen() #listens to the socket

socket.setblocking(True) #eliminates the blocking problem

selector.register(socket, selectors.EVENT_READ, data = None)

def accept_client(socket):
  connect, address = socket.accept()  # Should be ready to read
  connect.setblocking(False)
  data = types.SimpleNamespace(address = address, inbytes = b"", outbytes = b"")
  events = selectors.EVENT_READ | selectors.EVENT_WRITE #| = "or" in bytes
  selector.register(connect, events, data = data)

def check_connection(socket_object, ready_events):
  socket = socket_object.fileobj
  data = socket_object.data
  if ready_events and selectors.EVENT_READ: #if in read mode
    recieved_data = socket.recv(4096) #recieves a max amount of 4096
    if recieved_data:
      print("Recieved: "+str(recieved_data))
      data.outbytes += recieved_data #adds recieved data to out data
    else:
      print("Closing connection to"+str(socket))
      selector.unregister(socket)
      socket.close()
  if ready_events and selectors.EVENT_WRITE: #if in write mode
    if data.outbytes:
      sent_data = socket.send(data.outbytes)
      print("Sending "+str(sent_data)+" to "+str(socket))
      data.outbytes = data.outbytes[sent_data:] #adds sent_data to out_bytes

try:
  while True:
    events = selector.select(timeout = None)
    for socket_object, ready_events in events:
      if socket_object.data is None: #"is" checks if the object is the exact same (checks if there is no socket data and if not, it accepts the client)
        accept_client(socket_object.fileobj)
      else:
        check_connection(socket_object, ready_events)

finally:
  selector.close()
