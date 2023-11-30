import pyqrcode # must be installed using pip: pip install pyqrcode 
import socket

IP = "localhost"
port=12345 # random port number >1000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initializing a TCP socket since the app requires TCP
serverSocket.bind((IP, port))

def generateQR(url):
    qr = pyqrcode.create(url)

    #save file as png/svg
    png = qr.png("name_of_image.png", scale=4) # save the image of the QR code with name of the image

'''
    these lines of codes represent the initialization of the socket of the server and the function
    generateQR(url) will generate the QR as a png image and will later on send the image to the client 
    via the socket.
'''