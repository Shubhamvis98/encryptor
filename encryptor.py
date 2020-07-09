import base64
from os import rename as rn

def enc(file):
    # Encrypt
    with open(file, 'rb',) as img:
        cp = img.read()
        img.close()
        b64=base64.b64encode(cp)
        enc=b64.decode('ascii')

    # Write to file
    with open(file, 'w') as eimg:
        eimg.write(enc)
        rn(file, file + '_enc')

# File to encrypt
file = 'enc.jpg'

enc(file)