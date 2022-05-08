import socket 

SERVER_ADDRESS = ('localhost', 7007) 

class SocketClient():
    def __init__(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(SERVER_ADDRESS) 
    
    def start(self) -> None:
        try:
            print(self._client.recv(1024).decode('utf-8'))

            while True:
                message = input("message >").encode('utf-8')
                self._client.send(message)

                if message == 'quit':
                    self._client.close()
                    print('Bye!')
        except:
            self._client.close()
            print('Something is Wrong.')
        
client = SocketClient()
client.start()

    