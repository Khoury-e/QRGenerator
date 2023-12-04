import socket

IP = "localhost" 
port = 12345

client_socket = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP,port))

url = input("URL: ")

client_socket.send(url.encode())

file = open("QR.png","wb")
image_data = client_socket.recv(2048)

while image_data:
    file.write(image_data)
    image_data = client_socket.recv(2048)


file.close()

client_socket.close()

