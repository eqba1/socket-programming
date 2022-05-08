import socket

SERVER_IP='127.0.0.1'
SERVER_PORT=6000

"""
Creating a socket:
socket.socket (socket_family, socket_type, protocol=0)

list of socket_type: 
- TCP socket (Socket.SOCK STREAM)
- UDP sockets (Socket. SOCK DGRAM)

list of Socket Family:
- UNIX sockets, which were created before the network definition and are based on data
- Socket.AF INET
- Socket.AF INET6

You can get more information and find some examples usign this socket type
in the socket module documentation: https://docs.python.org/3/library/socket.html
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # family = Internet, type = stream socket means TCP            
server.bind((SERVER_IP,SERVER_PORT))                            # Bind the socket to a local address.

client = ''

try: 
    while True:
        if client == '':
            server.listen(1)                    # Enable a server to accept connections.
            print("Server Listening on {}:{}"\
                .format(SERVER_IP,SERVER_PORT))

            client, addr = server.accept()      # Wait for an incoming connection
            print(addr," got connected.")

            msg = "I am the server accepting \
            connections...".encode('utf-8')     # Handshake with Client
            client.send(msg)                    # Send a data string to the socket.

        request = client.recv(1024)             # Receive up to buffersize bytes from the socket. 
        request = request.decode('utf-8')       # Decoding
        print("[*] Received request: {}"\
            .format(request))

        if request == '':                       # Remove connection if client quit
            client = ''

except KeyboardInterrupt:
    print('\Wait')
    # client.send('Server is Down')
    server.close()                              # Close the socket.
    print('End.')