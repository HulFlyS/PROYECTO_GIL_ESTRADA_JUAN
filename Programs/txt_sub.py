#!/usr/bin/env python3

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  	
	print("Connected with result code "+str(rc))
  	client.subscribe("topic/num")
	client.subscribe("topic/name")
	client.subscribe("topic/date")

def on_message(client, userdata, msg):  	
  	
	values = msg.payload.decode()	
	
	file = open("file.txt","a")	
	file.write(""+values+"\n")
	file.close()
	
	print("Se inserto: "+values)
	  
client = mqtt.Client()
client.connect("85.137.205.6",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
