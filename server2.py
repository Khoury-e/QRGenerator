import socket
import pyqrcode
import threading # to handle multithreading

IP = "localhost" 
Port = 12345 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, Port))
serverSocket.listen(1)

'''to handle each client, for each client: 
1- get url 
2- generate QR code (as png)
3- send image 
4- close connection
'''

def handler(clientSocket, clientAddr):
    print("Connection from ", client_addr)
    url = clientSocket.recv(1024).decode()
    print("URL received: ", url)

    qr = pyqrcode.create(url)
    qr.png("QR.png", scale=6)

    with open("QR.png", "rb") as file:
        image_data = file.read(2048)

    clientSocket.sendall(image_data) # send the whole image instead of chunks (as done previously)
    
    clientSocket.close()
while True:
    print(f"Listening on IP {IP}, port {Port}")
    clientSocket, client_addr = serverSocket.accept()

    # start a new thread (like in OS in C)
    thread = threading.Thread(target=handler, args=(clientSocket, client_addr))
    # start thread
    thread.start()
    
serverSocket.close()
