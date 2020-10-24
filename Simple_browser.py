import socket
import sys

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.
    print("Socket created Succesfully")
except socket.error as err:
    print("Socket crestion failed\n Error :",err)

mysock.connect(('facebook.com', 80)) #80 is default port number

# Connect with IP address
try:
    host_ip=socket.gethostbyname("facebook.com")
except socket.gaierror:
    #It means it could not resolve host
    print("Error resolving the host")
    sys.exit()

#mysock.connect((host_ip,80))

print("The IP address of host is ",host_ip)
cmd = 'GET http://www.facebook.com HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
