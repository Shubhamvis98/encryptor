import base64, os, tkinter
from tkinter import messagebox as msg
from threading import Thread as thread
from os import rename as rn
from os import system as cmd

# hide main window
maingui = tkinter.Tk()
maingui.withdraw()

# clear screen
if os.name == 'nt':
    cmd('cls')
else:
    cmd('clear')

# decryptor
def dec(file):
    # Decrypt
    try:
        with open(file, 'r') as enc:
            cp = enc.read()
            enc.close()
            dec64 = cp.encode('ascii')
            dec = base64.b64decode(dec64)
            enc.close()
    except:
        print("[!] Error while openning file...", file)

    # Write to file
    with open(file, 'wb') as dimg:
        dimg.write(dec)
        dimg.close()
        fname = file.split(sep='_enc')[0]
        rn(file, fname)
# --END--

def driverun(root):
    for ROOT, DIR, FILE in os.walk(root, topdown=False):
        for name in FILE:
            PATH = os.path.join(ROOT, name)
            ext = PATH.split('.')[-1]
            if ext.lower() == 'jpg_enc' or ext.lower() == 'jpeg_enc' or ext.lower() == 'png_enc':
                print(PATH)
                #dec(PATH)
                thread(target=dec, args=(PATH,)).start()
        for name in DIR:
            PATH = os.path.join(ROOT, name)
            #operations with direstories

dr = [chr(i) for i in range(ord('D'), ord('Z')+1)]
drives = [d+':\\' for d in dr if os.path.exists(f'{d}:')]

for i in drives:
    #driverun(i)
    thread(target=driverun, args=(i,)).start()

msg.showinfo(title='Decryptor',message='Decryption Completed')
