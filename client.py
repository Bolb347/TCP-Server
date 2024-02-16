import socket

host = "127.0.0.1"#input("Enter the server host IP (127.0.0.1 if it is your computer): ")#"127.0.0.1" #need to change for connecting to a server not on your computer
port = 52000#input("Enter the server port number (4096 for this demonstration): ")#4096 #port: need to connect to the server port

socket = socket.socket()

socket.connect((host, port))
socket.settimeout(None)

while True:
    try:
        socket.sendall(b"connected")
    except:
        print("WARNING: could not send data: probably a server-side problem")
    print("recieved data: "+str(socket.recv(1024).decode('utf-8')))
