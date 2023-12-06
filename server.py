import socket
import pyqrcode
import threading

IP = "localhost"
Port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, Port))
serverSocket.listen(1)

def handler(clientSocket, clientAddr):
    print("Connection from ", clientAddr)
    url = clientSocket.recv(1024).decode()
    print("URL received: ", url)

    qr = pyqrcode.create(url)
    qr.png("QR.png", scale=6)

    with open("QR.png", "rb") as file:
        image_data = file.read(2048)

    clientSocket.sendall(image_data)

    clientSocket.close()

while True:
    print(f"Listening on IP {IP}, port {Port}")
    clientSocket, client_addr = serverSocket.accept()

    thread = threading.Thread(target=handler, args=(clientSocket, client_addr))
    thread.start()

serverSocket.close()
