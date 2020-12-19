# pip3 install qrcode
import qrcode
import uuid

mail='ubuntu_user@web.de'

uuid=uuid.uuid4()
s=uuid.hex
#s=f"{uuid.hex}\n{mail}"
print(s)

# code=qrcode.make(s)
# img = code.get_image()
# code.png('code.png', scale=4)
# code.show()

qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)
qr.add_data(s)
qr.make()
img = qr.make_image()
img.save('code.png')
