import socket

host = "127.0.0.1" #need to change for connecting to a server not on your computer
port = 4096 #port: need to connect to the server port

socket = socket.socket()

socket.connect(host, port)

def send_data(data): #sends data to server (needs to be in byte form before by using b"data")
  socket.sendall(data)

def recieve_bytes: #recieves and returns bytes from the server
  return socket.recv(4096)

def decode(bytes):
  return bytes.decode()

send_data(b"connected")
