import socket

#used for listening for the file coming in from the keylogger. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)

print(msg.decode("utf-8"))

# file_name = client.recv(1024).decode()
# print(file_name)
# file_size = client.revc(1024).decode()
# print(file_size)