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


image_matrix_str = client_socket.recv(1024).decode()  # receiving the 2D matrix from the server
image_matrix = np.fromstring(image_matrix_str, dtype=np.uint8)
#(assuming pixel values are in the range 0-255)

# Recommended dimensions for a square grayscale image
height, width = int(np.sqrt(len(image_matrix))), int(np.sqrt(len(image_matrix)))
image_data = image_matrix.reshape((height, width))

image = Image.fromarray(image_data, mode="L")  # "L" for grayscale
image.save("output_image.png")  # save the image
image.show()  # load the image

client_socket.close()