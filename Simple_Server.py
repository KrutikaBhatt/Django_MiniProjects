from socket import *

def createServer():
    serversocket=socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()

            receive=clientsocket.recv(5000).decode()
            pieces=receive.split("\n")
            if (len(pieces)>0) :
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello Developers...This is <h1>Krutika Bhatt</h1></body></html><p>This is a paragraph</p>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\n Shutting down the server ...\n");
    except Exception as err:
        print("Error ocurred\nError :",err);

    serversocket.close()

print('Access this link- http://localhost:9000')
createServer()

# The response u get is GET /favicon.ico HTTP/1.1
#It means that people with browsers that use favicon (Internet Explorer 5.0 +, Firefox, Opera and a most others) are visiting your site.

