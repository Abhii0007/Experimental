import socket,time
print('Server1\n\n')

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 8305

# bind the socket to a public host and a port
serversocket.bind((host, port))

# become a server socket
serversocket.listen(1)
print('Setup the connection\n\n')

while True:
    # establish a connection
    abhi_input=str(input('Type the message for client = '))
    
    
    try:
        clientsocket, addr = serversocket.accept()
    
    #print("Got a connection from %s" % str(addr))

 
        message = abhi_input 
        clientsocket.send(message.encode('ascii'))
        
        print('Message Sent','-'*70)
    except:
        print('Not Sent\n')
    #clientsocket.close()
