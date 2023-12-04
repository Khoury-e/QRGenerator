import socket
import pyqrcode

IP="localhost"
Port=12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, Port))

    
while True:
    print(f"Listening on IP {IP}, port {Port}")
    serverSocket.listen(1)
    clientSocket, client_addr = serverSocket.accept()
    
    print("Connection from ", client_addr)
    url = clientSocket.recv(1024).decode()
    print("URL received: ", url)
    
    qr = pyqrcode.create(url)
    png = qr.png("QR.png", scale=6)

    file = open("QR.png", "rb")
    image_data = file.read(2048)
    
    while image_data:
        clientSocket.send(image_data)
        image_data = file.read(2048) 
    
    file.close()
        
    
clientSocket.close()
serverSocket.close()    
    