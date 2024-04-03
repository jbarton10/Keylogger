import socket

#used for listening for the file coming in from the keylogger. 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.revc(1024).decode()
print(file_size)
