import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

s.send("01Uuuuuhhhhhhhhhhhhhhhhh".encode("utf-8"))

while True:
    data = s.recv(1024)
    if data:
        print('Received: ' + data.decode('utf-8'))
