import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)

qr.add_data('hi twitter')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save('out.png')
