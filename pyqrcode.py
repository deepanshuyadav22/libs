import pyqrcode
import png

s = "Deepanshu Yadav"

qrcode = pyqrcode.create(s)

qrcode.png('dy.png', scale = 8)
#qrcode.png('dy.svg', scale = 8)

#https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
