import socket
server_ip = "localhost"
server_port = 12345 # random socket number that is the server's sockrt number
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #This code creates a TCP client socket for IPv4 communication
client_socket.connect((server_ip,server_port)) #connecting to the server socket
url = input("Please Enter the URL: ")
client_socket.send(url.encode())

