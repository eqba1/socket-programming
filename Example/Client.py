import socket
import logging


logger = logging.getLogger(__name__)

SERVER_IP='127.0.0.1'                   # The Server ip address.
SERVER_PORT=6000                        # The Server Port number.

def is_socket_closed(sock: socket.socket) -> bool:
    try:
        # this will try to read bytes without blocking and also without removing them from buffer (peek only)
        data = sock.recv(16, socket.MSG_DONTWAIT | socket.MSG_PEEK)
        if len(data) == 0:
            logger.exception("Server is Down")
            return True

    except BlockingIOError:
        return False  # socket is open and reading from it would block
    except ConnectionResetError:
        logger.exception("SERVER is Down")
        return True  # socket was closed for some other reason
    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        return False
    return False

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # family = Internet, type = stream socket means TCP.

    mysocket.connect((SERVER_IP, SERVER_PORT))                      # Connect the socket to a remote address.
    print('Connected to host {} in port: {}'\
        .format(SERVER_IP, SERVER_PORT))

    msg = mysocket.recv(1024)                                       # Receive up to buffersize bytes from the socket.
    print("Message received from the server:", msg)

    while not is_socket_closed(mysocket): 
        # print(mysocket)                                            
        message = input("Enter your message > ")                    # Imput Message.
        mysocket.send(bytes(message.encode('utf-8')))               # Send a data string to the socket.
        
        if message == "quit": 
            mysocket.close()
            print("Bye!")
            break
        
except KeyboardInterrupt:
    mysocket.close()                        # Close the socket.
    print("End.")

