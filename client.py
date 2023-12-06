import socket
import sys
import tkinter as tk
from tkinter import Entry, Label, Button, Toplevel
import threading
from PIL import Image, ImageTk  # Pillow library for image processing

def send_url():
    url = url_entry.get()
    client_socket.send(url.encode())

    file = open("QR.png", "wb")
    image_data = client_socket.recv(2048)

    while image_data:
        file.write(image_data)
        image_data = client_socket.recv(2048)

    file.close()

    # Display QR code in a new window
    qr_image = Image.open("QR.png")
    qr_image = qr_image.resize((300, 300), Image.BILINEAR)
    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_window = Toplevel()
    qr_window.title("Generated QR Code")

    label = tk.Label(qr_window, image=qr_photo)
    label.image = qr_photo
    label.pack()

def create_gui():
    window = tk.Tk()
    window.title("QR Code Generator")
    window.geometry("400x200")  # Set the size of the GUI

    label = Label(window, text="Enter URL:")
    label.pack(pady=10)

    global url_entry
    url_entry = Entry(window, width=30)
    url_entry.pack(pady=10)

    send_button = Button(window, text="Generate QR Code", command=send_url)
    send_button.pack(pady=10)

    window.mainloop()

IP = "localhost"
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, port))

gui_thread = threading.Thread(target=create_gui)
gui_thread.start()

gui_thread.join()

client_socket.close()
sys.exit()
