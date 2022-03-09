import socket

SERVER_IP='127.0.0.1'                   # The Server ip address.
SERVER_PORT=5000                        # The Server Port number.

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # family = Internet, type = stream socket means TCP.

    mysocket.connect((SERVER_IP, SERVER_PORT))                      # Connect the socket to a remote address.
    print('Connected to host {} in port: {}'\
        .format(SERVER_IP, SERVER_PORT))

    msg = mysocket.recv(1024)                                       # Receive up to buffersize bytes from the socket.
    print("Message received from the server:", msg)

    while True:                                                      
        message = input("Enter your message > ")                    # Imput Message.
        mysocket.send(bytes(message.encode('utf-8')))               # Send a data string to the socket.
        
        if message== "quit":
            break
        
except KeyboardInterrupt:
    mysocket.close()                        # Close the socket.
    print("End.")

