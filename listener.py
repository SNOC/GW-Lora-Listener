#  This script allows listening to UDP request on port 15555
#
#  V1.1 can receive keepAlive or Data, and display it on the console
#  Run this program and wait for incomming UDP packets

import sys
import socket
import json
import base64


# OPENING SOCKET ON PORT 15555
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('', 15555))

cur_version = sys.version_info # base64.decode differs from python 2.7 to 3.x

print("Gateway listener starts\n")
data = bytearray(480)

while True: # NEVER STOP
    
    nbytes,addr = socket.recvfrom_into(data, 480)

    if( nbytes > 0 ):
        macAddress=""
        for i in range(4, 9):
            macAddress += '{:02X}'.format(data[i]) + ":"
        macAddress += '{:02X}'.format(data[9]) # do not add ":" after last char
                        
        if( nbytes == 12 ):
            #KEEPALIVE MESSAGE HAS A LENGTH = 12
            print("KeepAlive received from : "+macAddress+"\n")
        else :
            #DATA TRANSMITTED    
            data2=data[12:nbytes].decode('utf8') #THIS IS THE DATA PART
            dico = json.loads(data2) #AFFECT TO JSON OBJECT
            list = dico["lwpk"] #CONVERT TO LIST FORMAT
            dic=list[0] #GET FIRST ITEM OF DICTIONNARY
                
            print("Data received from gateway : "+macAddress)
            print("Sent from device : "+dic['deui'])
            
            size = dic['size']
            secret = dic['data']
            message=""
                    
            msgdec=base64.b64decode(secret, altchars=None) #DECODE MESSAGE
            if( cur_version >= (3, 0) ):
                for char in msgdec: #FOR EACH BYTE 
                    message += '{:02X}'.format(char)
            else:
                 for char in msgdec: #FOR EACH CHAR 
                    message += '{:02X}'.format(ord(char))
                   
            print("Decoded message : "+message)
            print("JSON : "+data2+"\n")
            
