import socket
import sys

#Step 1: read command line arguments, IP and port
serverIP = str(sys.argv[2])
port = int(sys.argv[4])
logFileDestination = str(sys.argv[6])

#Step 2: Create a socket object, use TCP socket(SOCK_STREAM) for this assignment
client_socket = socket.socket(type = socket.SOCK_STREAM)

#Step 3: Connect to the IP and port read from command line
try:
    client_socket.connect((serverIP, port))
except ConnectionRefusedError as e:
    print(e)
    sys.exit(1)

# Step 4: read a message from user
message = input("Enter a message: ")
message_bytes = message.encode('utf-8')

# Step 5: send message to the server
client_socket.sendall(message_bytes)

# Step 6: receive message from the server
response = client_socket.recv(1024).decode()
print(response)

logfile = open(logFileDestination, 'w')
print(response, file = logfile)
logfile.close()

# close the socket
client_socket.close()