import socket.threading
serverSocket = socket.socket()
serverSocket.bind(("192.168.0.153",5001))

class clientMessage(threading.Thread):
    def __init__(self,socket,address):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.start()
    def run(self):
        while True:
            value = self.socket.recv(1024).decode()
            #value=value.split(",")
            print(value)
            self.socket.send("Message recieved".encode('ascii'))
server.listen(5)
while True:
    s.address = serverSocket.accept()
    client.Message(s,address)
serverSocket.close()
    
