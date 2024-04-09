import socket
import sys

#Find a way to keep this running constantly so that things can be stored ad show up over time. 

def openListener():
    
    #used for listening for the file coming in from the keylogger. 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))

    msg = s.recv(1024)

    print(msg.decode("utf-8"))

    file_name = s.recv(1024).decode()
    print(file_name)
    
def getInput():
    getFile = input("Recieve key log file? (Yes or No)  ")

    if getFile.lower() == "yes":
        
        #Run listner
        openListener()
        getInput()


    elif getFile.lower() ==  "no":

        #Exit program
        print("Thanks for listnening!  xD")
        sys.exit()
    else:
        
        #For wrong user input
        print("We only take yes and no as input, thanks!\n")
        getInput()


def main():
    getInput()

if __name__ == "__main__":
    main()


#Should write file_name to a file so it can be saved more reliably

