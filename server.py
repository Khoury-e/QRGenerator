import pyqrcode # must be installed using pip: pip install pyqrcode 
import socket
from PIL import Image
import numpy as np

IP = "localhost"
port=12345 # random port number >1000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initializing a TCP socket since the app requires TCP
serverSocket.bind((IP, port))

def generateQR(url):
    qr = pyqrcode.create(url)

    #save file as png/svg
    png = qr.png("name_of_image.png", scale=4) # save the image of the QR code with name of the image
    
    image_array = np.array(png) # turn the image into a numpy array
    return image_array # returning the image

serverSocket.listen (1)
print (" Server listening on", IP , port )
# Accept client ’s connection
client_socket , client_address = port.accept()
print (" Accepted connection from ", client_address)
url = client_socket.recv(1024).decode()
print (" Received from client ", url)

image_matrix = generateQR(url)
client_socket.send( image_matrix.encode())


client_socket.close()
serverSocket.close()
'''
    these lines of codes represent the initialization of the socket of the server and the function
    generateQR(url) will generate the QR as a png image and will later on send the image to the client 
    via the socket.
'''