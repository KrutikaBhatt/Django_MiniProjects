import socket

try:
    mysocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Succesfully\n\n")
except socket.error as err:
    print("Error occured :",err)

mysocket.connect(('127.0.0.1',9000))
cmd='GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# Request-Line   = Method SP Request-URI SP HTTP-Version CRLF
# GET method, Request -URL:http://127.0.0.1/romeo.txt ,HTTP-Version:HTTP/1.0
mysocket.sendall(cmd)
while True:
    data = mysocket.recv(512)
    if (len(data)<1):
        print("Shutting down the socket ")
        break
    else:
        print(data.decode(),end="")

mysocket.close()

# A Even Simple Client
#import urllib.request

#request_url = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
#for line in request_url:
#    print(line.decode().strip())


