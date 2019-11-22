import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.1', 80))

init = '\x01\x02\x03\x04'

s.sendall(init + '\x00')

data = s.recv(1024)
print 'Received', repr(data)
s.close()
