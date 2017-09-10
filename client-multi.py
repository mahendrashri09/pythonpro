import socket.threading
s = socket.socket()
s.connect(("192.168.0.153",5001))
while True:
    data = input("Client> ")
    if data == 'exit': exit()
    else:s.send(data.encode("ascii"))
    data = s.recv(1024)
    print(data.decode('ascii'))
s.close()

