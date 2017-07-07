# GW UDP listener

##### This script receives and displays UDP data from Nemeus Lora pico Gateway. It displays keepAlive and data frame.

Lora devices can be purchased on [YADOM.FR]
(https://yadom.fr/).

One python script is provided :

- listener.py which is the script that listens to UDP packets.

##### Usage

- Run the script on a python interpreter, incomming messages will be displayed on the console.

##### Prerequist

Python interpreter 2.5 or higher

##### Interface

The script can show two kinds of messages :

-if the transmitter sends a keepAlive request, the script will display the gateway EUI

-if the transmitter sends a data packet, the script will display the gateway mac adress, transmitter id, received data and JSON sent by the Lora Gateway.

##### License

MIT License / read license.txt
