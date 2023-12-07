import socket
import pyqrcode
import threading
import json 

IP = "localhost"
Port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, Port))
serverSocket.listen(1)

def handler(clientSocket, clientAddr):
    print("Connection from ", clientAddr)
    username = clientSocket.recv(1024).decode()
    password = clientSocket.recv(1024).decode()
    
    print(f"Username: {username}, Password: {password}")
    with open('Users.json','r') as file:
        users = json.load(file)
        
        for i in range(len(users)):
            if users[i]["username"] == username and users[i]["password"]==password:
                clientSocket.send("Granted".encode())
                
                # the user is properly signed in
                # get url and send QR Code
                url=clientSocket.recv(1024).decode()
                print(f"URL Received: {url}")
                
                qr = pyqrcode.create(url)
                qr.png("QR.png", scale=6)
                with open("QR.png", "rb") as file:
                    image_data = file.read(2048)
                clientSocket.sendall(image_data)
                
            else:
                clientSocket.send("Denied".encode())
    

    clientSocket.close()

while True:
    print(f"Listening on IP {IP}, port {Port}")
    clientSocket, client_addr = serverSocket.accept()

    thread = threading.Thread(target=handler, args=(clientSocket, client_addr))
    thread.start()

serverSocket.close()
