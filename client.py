import socket
import sys
import tkinter as tk
from tkinter import Entry, Label, Button, Toplevel, messagebox
import threading
from PIL import Image, ImageTk  # Pillow library for image processing

def send_credentials():
    username = username_value.get()
    password = password_value.get()
    
    # send username and password to server
    client_socket.send(username.encode())
    client_socket.send(password.encode())
    
    # get the response (grant permission/deny permission)
    permission = client_socket.recv(1024).decode()
    if permission.lower() == "granted":
        login()
    else:
        tk.messagebox.showerror(message="Wrong username or password", title="Error In Log In")

def login():
    for widget in window.winfo_children():
        widget.destroy()
    label = Label(window, text="Enter URL:")
    label.pack(pady=10)

    global url_entry
    url_entry = Entry(window, width=30)
    url_entry.pack(pady=10)

    send_button = Button(window, text="Generate QR Code", command=send_url)
    send_button.pack(pady=10)

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
    global window
    window = tk.Tk()
    window.title("QR Code Generator")
    window.geometry("400x200")  # Set the size of the GUI

    # handle sign in mechanism before granting access to generate QR Code
    username = Label(window, text="Username:")
    username.pack()
    
    global username_value 
    global password_value
    
    username_value= Entry(window, width=30)
    username_value.pack()
    
    password = Label(window, text="Password:")
    password.pack()

    password_value = Entry(window, width=30)
    password_value.pack()
    
    login_button = Button(window, text="Log In", command=send_credentials)
    login_button.pack(pady=10)
    
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
