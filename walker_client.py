##############################################
# Created by Mitch Walker in May 2026
# CS 3622
#
# Client script for echo server
##############################################

import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1" # Uses the ip addres specified when running the script. If none is specified, assume the script is being tested locally
PORT = 65432

# Creates the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:# Create socket object, AF_INET is for IPv4, SOCK_STREAM is for TCP
    sock.connect((HOST, PORT))     # Connects the socket to the host and port
    while True:
        msg = input("Enter a message to send to the server (or 'End' to quit): ") # Gets user input
        sock.sendall(msg.encode())          # Encodes and sends message to server
        data = sock.recv(1024)              # Waits to recieve data from server
        print(f"Received {data.decode()}")  # Decodes and prints message from server
        
        # Breaks out of the loop if user inputs "End"
        if msg.casefold() == "end":
            break