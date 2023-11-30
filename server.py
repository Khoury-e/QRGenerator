import pyqrcode # must be installed using pip: pip install pyqrcode 

url = 'http://www.example.com' # any valid url
qr = pyqrcode.create(url)

#save file as png/svg
png = qr.png("name_of_image.png", scale=4) # save the image of the QR code with name of the image