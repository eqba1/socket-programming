import socket

class SocketServer():
    def __init__(self) -> None:
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 7007

        try:
            self._server.bind((self.host, self.port))
        except OSError:         
            print("Something goes wrong.")
            print("Try another IP or Port number.")
            exit(0)
        
        self._server.listen(1)

    def start(self) -> None:
        connection = None
        try:
            while True:
                if connection is None:
                    connection, address = self._server.accept()
                    print(address, "got connected")
                    connection.send("Connected Successfuly".encode('utf-8'))

                request = connection.recv(1024)
                request = request.decode('utf-8')
                print("[*] Reciverd from client:{}".format(request))

                if request == '' or request == "quit":
                   connection, address = None
                   print("[*] {} left the server".format(address))

        except:
            print("Wait")
            self._server.close()
            print("Bye!")

my_server = SocketServer()
my_server.start()