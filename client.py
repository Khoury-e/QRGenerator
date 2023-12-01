import socket
from PIL import Image # used to decode the image
# use pip install pillow
import numpy as np # pip install numpy
server_ip = "localhost"
server_port = 12345 # random socket number that is the server's sockrt number
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #This code creates a TCP client socket for IPv4 communication
client_socket.connect((server_ip,server_port)) #connecting to the server socket
url = input("Please Enter the URL: ") #taking the url as input
client_socket.send(url.encode()) # sending the url

image_matrix = client_socket.recv(1024).decode() # reciving the 2d matrix from the server
image_data = np.uint8(image_matrix)# Convert the matrix to uint8 data type 
#(assuming pixel values are in the range 0-255)

image = Image.fromarray(image_data)# Create an image from the matrix

image.save("output_image.png") # save the image
image.show() #load the image

