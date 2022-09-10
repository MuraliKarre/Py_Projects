import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
user_input = str(input("Enter the Text to convert QRCode: "))

# Generate QR code
url = pyqrcode.create(user_input)

# Create and save the png file naming "myqr.png"
url.svg("Murali.svg", scale=15)