##############################################
# Created by Mitch Walker in May 2026
# CS 3622
#
# Echo server script
##############################################

import socket

def reverse_string(str):
    return str[::-1]

HOST = ""
PORT = 65432

# Creates the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:# Create socket object, AF_INET is for IPv4, SOCK_STREAM is for TCP
    sock.bind((HOST, PORT))     # Binds the socket to the host and port
    sock.listen()               # Listens for incoming connections    
    conn, addr = sock.accept()  # Creates a connection object and gets the address of the client
    with conn:
        print(f"Connected by {addr}")
        
        while True:
            data    = conn.recv(1024)       # Waits to recieve data from client
            msg     = data.decode()         # Decodes message
            print(f"Received: {msg}")       # Prints recieved message
            revMsg  = reverse_string(msg)   # Reverses message
            conn.sendall(revMsg.encode())   # Sends reversed message to client

            if msg.casefold() == "end":     # Breaks out of the loop if client sends "end" 
                break