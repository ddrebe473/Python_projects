import socket  # Importing the socket module to create network sockets

# Defining the host and port to connect to
HOST = '127.0.0.1'  # Localhost IP address
PORT = '8080'  # Port number to connect to

# Creating a client socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connecting the client socket to the host and port
client_socket.connect((HOST, int(PORT)))

# Receiving the message from the server and decoding it
message = client_socket.recv(1024)
message = message.decode('utf-8')

print(message)

