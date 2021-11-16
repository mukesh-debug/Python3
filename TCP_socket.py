#!/usr/bin/env python3
import socket #socket library is consists required class and functions for making tcp connections

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#my_sock gets assigned an object equivalent to transport layer

#to make connection to the webserver using commonly used port i.e port 80
HOST = 'data.pr4e.org'
PORT = 80
my_sock.connect((HOST, PORT)) #A tuple of host and port is given as argument to connect member func of the obj

#To send the GET request to the webserver use send member func on the obj
my_sock.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode())
#The format is 'Method RequestURL HTTPVersion CRLF'
#CRLF is a single empty line '\r\n\r\n', here '\r\n' means eof(end of file) character

#now we should get the data from the webserver
while True:
  data = my_sock.recv(100) #here arg to recv func is the number of bytes of data to receive in one go
  if(len(data) < 1): # if data is not received break out of the while loop
    break
  print(data.decode()) # here decode func is used to convert the byte data to string type data
my_sock.close() #now we should close the connection to the webserver


#The same file can be accessed by using telnet tool also like
#'$telnet data.pr4e.org 80' and then issuing a GET method as 
#'GET http://data.pr4e.org/romeo.txt HTTP/1.0' and then pressing <enter> to indicate a blank line
#now you will be able to get the same data from the webserver
