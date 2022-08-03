import pyqrcode as qr
from pyqrcode import QRCode

QR_TEXT=(input("Entre Text to convert into QR Code = :"))

Qr=gen=qr.create(QR_TEXT)

Qr.svg("QRCODE"+QR_TEXT[0:4]+'.SVG',scale=8)