import socket
 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
 
while True:
    command = raw_input(">>>")
    print 'you command',command,type(command)
    if command == "q":
        client.sendall(command)
        break
    else:
        client.sendall(command)
        # data = client.recv(1024)
        # print data