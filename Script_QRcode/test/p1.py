import pyqrcode

FILE_PNG_1 = "qrcode1.png"
FILE_PNG_2 = "qrcode2.png"

# QRコードの作成1
code = pyqrcode.create(
    "https://github.com/EtoEto32", error="L", version=3, mode="binary"
)
code.png(FILE_PNG_1, scale=5, module_color=[0, 0, 0, 128], background=[255, 255, 255])

# QRコードの作成2
code = pyqrcode.create(
    "https://github.com/EtoEto32", error="L", version=3, mode="binary"
)
code.png(FILE_PNG_2, scale=5, module_color=[0, 0, 0, 128], background=[255, 255, 255])
