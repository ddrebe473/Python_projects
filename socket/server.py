import socket  # Importing the socket module to create network sockets

# Prompting the user to enter a message to send to the server
msg = input("Please enter your message ")

# Defining the host and port to listen on
HOST = '127.0.0.1'  # Localhost IP address
PORT = '8080'  # Port number to listen on

# Characters to encrypt
chars = "abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*"

# Encryption key
key = "password"
val = chars[::-1]
encriptor = dict(zip(key, val))

# Encrypting the message entered by the user
encripted_msg = ""
for word in msg.lower():
    if word in key:
        encripted_msg += val[key.index(word)]
    else:
        encripted_msg += word

# Creating a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket object to the host and port
server.bind((HOST, int(PORT)))

# Listening for incoming connections from clients, with a maximum queue of 5 clients
server.listen(5)

# Infinite loop to keep the server running
while True:
    # Accepting incoming connection from client and getting the communication socket and client address
    communication_socket, address = server.accept()

    # Sending the encrypted message to the client
    communication_socket.send(bytes(msg, 'utf-8'))
