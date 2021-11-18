#!/usr/bin/env python3

import socket  # Socket library for data retrieval

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# created socket to establish connection through

my_socket.connect(('data.pr4e.org', 80)) # To make connection through the socket
http_protocol = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# method url protocol<eol><newline>
# data needs to be encoded from unicode to utf-8 to send over the socket

my_socket.send(http_protocol)  # Send the command to webserver

# To receive the data from the webserver
count = 1 
packet_size = 100
while True:
    data = my_socket.recv(packet_size)  # To receive 200 bytes of data in one go
    if not data:
        break
    print("[Packet", count, "](", packet_size, "bytes)")
    count +=1
    print(data.decode())
    print()

my_socket.close()  # Close the connection via socket to the webserver
