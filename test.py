#gererating a qr code to this website
import qrcode

data = "https://buzzer.lulusms.com/slideshow.php"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# Add data to the QR code object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save('qrcode.png')

# Optionally, display the image
img.show()
print("--"*80 + "finished")
