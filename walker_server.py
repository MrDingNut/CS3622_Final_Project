##############################################
# Created by Mitch Walker in May 2026
# CS 3622
#
# Echo server script
##############################################

import socket

def reverse_string(str):
    return str[::-1]

HOST = "127.0.0.1"
PORT = 65432

# Creates the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))
sock.listen()
conn, addr = sock.accept()
with conn:
    print(f"Connected by {addr}")
    
    while True:
        data = conn.recv(1024)          # Waits to recieve data from client
        msg = data.decode               # Decodes message
        revMsg = reverse_string(msg)    # Reverses message
        conn.sendall(revMsg.encode())   # Sends reversed message to client

        if msg.casefold() == "end":     # Breaks out of the loop if client sends "end" 
            break

    conn.close()    # Closes connection


