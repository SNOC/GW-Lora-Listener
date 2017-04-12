# GW UDP listener

##### Aim of this script is to receive and display UDP data from Nemeus Lora pico Gateway. It displays keepAlive and data frame.

Lora devices can be purchased on [YADOM.FR]
(https://yadom.fr/).

One python script is provided :

- listener.py which is the script that listen UDP signals.

##### Usage

-You just need to launch the script on a python interpreter, and the message will be set on the console.

##### Prerequist

Python interpreter 

##### Interface

The script can show two kind of messages :

-if the transmitter send a keepAlive request, the script will tell you and give the gw mac adress

-if the transmitter send a data packet, the script will tell you the gw adress, the id of the transmitter, the data received and the JSON sent by the Lora Gateway.

##### License

MIT License / read license.txt