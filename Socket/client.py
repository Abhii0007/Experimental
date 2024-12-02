import socket,time,os
print('Client1','\n\n')
print('Connecting to the server')
try:
    
    
    while True:

        # create a socket object
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()

        port = 8305

        # connection to hostname on the port.
        clientsocket.connect((host, port))
        

        # Receive no more than 1024 bytes
        msg_Encrypted = clientsocket.recv(1024)
        msg=msg_Encrypted.decode('ascii')
        #clientsocket.close()
        print(msg)
        print('-'*70)
        if msg=='green':
            os.system('color 02')
        elif msg=='blue':
            os.system('color 03')
        elif msg=='close':
            os.system('exit')

     
except:
    print('\nNo Server found')
    time.sleep(3)