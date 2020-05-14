import pyqrcode
from PIL import Image
import png

# TODO make into a function with url and image strings + filename of finalprodut
# TODO add way of iterating over barcodes

# make QR code from custom string
qrobj = pyqrcode.QRCode('https://fvvianello.github.io/pymol_ar/', error='H')
with open('output/test2_qr.png', 'wb') as f:
    qrobj.png(f, scale=10)

# open the QR code to place the logo in the middle
img = Image.open('output/test2_qr.png')
width, height = img.size

# open the logo image
logo = Image.open('barcodes/06-barcode.png')

# place logo
logo_size = 150
xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))
logo = logo.resize((xmax - xmin, ymax - ymin))
img.paste(logo, (xmin, ymin, xmax, ymax))
img.save('output/test2_qr.png')
