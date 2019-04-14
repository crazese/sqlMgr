import SocketServer
import permutation 

class SQLMgr(object):
    clientSocket = {}
    clientCommand = {}
    def __init__(self,request,client_address):
        self.request = request
        self.client_address = client_address
        print 'connect come'

    def sendOneClient(self, clientid, command):
        self.clientSocket[clientid].sendall(command)

    def recv(self):
        data = self.skt.recv(1024).strip()
        return data

    def addCommand(self, clientid, command):
        self.clientCommand[clientid] = command

    def addSocket(self, clientid, skt):
        self.clientSocket[clientid] = skt

    def excuteCommand(self):
        print 'start excute sql command ...'
        commandlist = permutation.getCommandList(self.clientCommand)
        print commandlist,self.clientCommand
        # commandlist: [['client1', 'client1', 'clien2'], ['client1', 'clien2', 'client1'], ['clien2', 'client1', 'client1']]
        for cmdSeq in commandlist:
            print 'one sequence start ...',cmdSeq
            clientidList = self.clientCommand.keys()
            clientidCountDict = dict(zip(clientidList,[0]*len(clientidList)))
            for clientIndex in cmdSeq:
                count = clientidCountDict[clientIndex]
                self.sendOneClient(clientIndex,self.clientCommand[clientIndex][count])
                clientidCountDict[clientIndex] = clientidCountDict[clientIndex]+1

    def handle(self):
        try:
            data = self.request.recv(1024).strip()
            if not data or data == 'exit':
                self.request.close()
                return
            elif data == 'start':
                self.excuteCommand()
            else:
                print('->client:', data,self.client_address)
                self.addSocket(self.client_address,self.request)
                self.request.send('connect success and upload the command!')
                if '#' in data:
                    command = data.split('#')
                else:
                    command = [data]
                self.addCommand(self.client_address,command)
            self.handle()
        except:
            print 'exception cause'
        self.request.close()




class CMDServer(SocketServer.BaseRequestHandler):
    def handle(self):
        self.socket = SQLMgr(self.request,self.client_address)
        self.socket.handle()
        # self.socket.excuteCommand()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
 
    server = SocketServer.ThreadingTCPServer((HOST, PORT), CMDServer)
 
    server.serve_forever()