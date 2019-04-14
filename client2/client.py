import socket
 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
 
def readSqlFile(file):
    with open(file,'rb') as f:
        command = f.read().splitlines()
    return command

# print '#'.join(readSqlFile('sql2.txt'))
client.send('#'.join(readSqlFile('sql2.txt')))
while True:
    data = client.recv(1024)
    if len(data)>1:print(len(data),data)
