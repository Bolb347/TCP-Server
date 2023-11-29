import socket

host = "127.0.0.1"#input("Enter the server host IP (127.0.0.1 if it is your computer): ")#"127.0.0.1" #need to change for connecting to a server not on your computer
port = 4096#input("Enter the server port number (4096 for this demonstration): ")#4096 #port: need to connect to the server port

socket = socket.socket()

socket.connect((host, port))

def send_data(data): #sends data to server (needs to be in byte form before by using b"data")
  socket.sendall(data)

def recieve_bytes(): #recieves and returns bytes from the server
  return socket.recv(4096)

def decode(bytes):
  return bytes.decode()

while True:
  send_data(b"connected")
  print("recieved data: "+str(decode(recieve_bytes())))
