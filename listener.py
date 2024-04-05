import socket

#used for listening for the file coming in from the keylogger. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
s.connect((host, port))

msg = s.recv(1024)

print(msg.decode("utf-8"))

file_name = s.recv(1024).decode()
print(file_name)
#file_size = s.revc(1024).decode()
# print(file_size)