#  This script allow to listen UDP request on the 15555 port 
#
#  V1.0 can receive keepAlive or Data, and show it on the console
#  You only need to run this program and wait for input



import socket
import json
import base64


#OPENING THE SOCKET ON THE 15555 PORT
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('', 15555))


while True: #NEVER STOP
    
    
    data,addr = socket.recvfrom(480) #WE ARE LISTENING
        
    i=0
    adresseMac=""
            
    for char in data:
        #FIND MAC ADRESS
        if(i>3 and i<10): 
            caracHexa = hex(char)
            caracHexa = caracHexa[2:4] #WE ONLY TAKE THE AB FROM 0XAB
            if(i==9):
                adresseMac = adresseMac + caracHexa
            else :
                adresseMac = adresseMac + caracHexa +":"
            i=i+1
        else :
            i=i+1
                    
                    
                    
                    
                    
    if(len(data)==12):
        #KEEPALIVE MESSAGE HAS A LENTH + 12
        print("keepAlive receveied from "+adresseMac+"\n")
    else :
        #DATA TRANSMITTED    
        donnee2=data[12:].decode('utf8') #THIS IS THE DATA
        dico = json.loads(donnee2) #IN JSON FORMAT
        liste = dico["lwpk"] #GIVE US A LISTE
        dic=liste[0] #GET THE DICTIONNARY
            
        print("Data received from gateway : "+adresseMac)
        print("Sent from "+dic['deui'])
        
        size = dic['size']
        secret = dic['data']
        x=0
        msgfini=""
                
        msgdec=base64.b64decode(secret, altchars=None, validate=False) #DECODING THE MESSAGE
        for char in msgdec: #FOR EACH BYTE 
            byte = hex(char)
            byte = byte[2:4]
            msgfini=msgfini+byte+" "

                
        print("DATA : "+msgfini)
        print("JSON value sent : "+donnee2+"\n")
            
            
            
            
        


        
