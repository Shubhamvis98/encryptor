import base64
from os import rename as rn

def dec(file):
    # Decrypt
    with open(file, 'r') as enc:
        cp = enc.read()
        enc.close()
        dec64 = cp.encode('ascii')
        dec = base64.b64decode(dec64)
        enc.close()

    # Write to file
    with open(file, 'wb') as dimg:
        dimg.write(dec)
        fname = file.split(sep='_')[0]
        rn(file, fname)

# File to encrypt
file = 'enc.jpg_enc'

dec(file)
