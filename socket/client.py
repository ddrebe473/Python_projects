import socket  # Importing the socket module to create network sockets

# Prompting the user to provide the encryption key
dec_key = input("give the encryption key: ")

# Defining the host and port to connect to
HOST = '127.0.0.1'  # Localhost IP address
PORT = '8080'  # Port number to connect to

# Defining the character set to use for encryption
chars = "abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*"

# Creating a client socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the client socket to the host and port
client_socket.connect((HOST, int(PORT)))

# Receiving the message from the server and decoding it
message = client_socket.recv(1024)
message = message.decode('utf-8')

# Reversing the encryption key and creating a decryption dictionary using it
val = chars[::-1]
decriptor = dict(zip(val, dec_key))

# Decrypting the message using the decryption dictionary
decrypted_message = ""
for char in message:
    if char in decriptor:
        decrypted_message += decriptor[char]
    else:
        decrypted_message += char

print("Decrypted message:", decrypted_message)

# Closing the client socket
client_socket.close()
