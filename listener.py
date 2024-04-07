import socket

#Find a way to keep this running constantly so that things can be stored ad show up over time. 

#used for listening for the file coming in from the keylogger. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
s.connect((host, port))

msg = s.recv(1024)

print(msg.decode("utf-8"))

file_name = s.recv(1024).decode()
print(file_name)

#Should write file_name to a file so it can be saved more reliably

