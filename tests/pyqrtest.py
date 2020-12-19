import pyqrcode
import uuid

s=uuid.uuid4().hex
print(s)
code = pyqrcode.create(s)
code.png("file.png", scale=4,  module_color=[0, 0, 0, 255], background=[100,64,64])
print(code.terminal(quiet_zone=1))