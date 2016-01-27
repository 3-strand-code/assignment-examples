import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('RECEIVED: ' + str(self.data))
        self.request.sendall(str(self.data).encode('utf-8'))


if __name__ == "__main__":
    server = socketserver.TCPServer(('localhost', 9999), MyTCPHandler)
    # if we don't allow reuse, can get errors restarting server quickly
    server.allow_reuse_address = True
    server.serve_forever()
