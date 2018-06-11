#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from pylab import *

def on_connect(client, userdata, flags, rc):
  	
	print("Connected with result code "+str(rc))
  	client.subscribe("topic/num")

def on_message(client, userdata, msg):  	
  	
	values = msg.payload.decode()

	print("Se inserto: "+values)	
		
	title('Grafica') 
	xlabel('Eje X') 
	ylabel('Eje Y')
	
	plt.plot(values, 'ro') 	
    	print(plt.show())
		
client = mqtt.Client()
client.connect("85.137.205.6",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
