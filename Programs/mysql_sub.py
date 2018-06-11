#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import MySQLdb 

def on_connect(client, userdata, flags, rc):
  	
	print("Connected with result code "+str(rc))
  	client.subscribe("topic/num")
	client.subscribe("topic/name")
	client.subscribe("topic/date")

def on_message(client, userdata, msg):  	
  	
	values = msg.payload.decode()	
	
	print("Se inserto: "+values)
	
	db=MySQLdb.connect(host='localhost',user='user',passwd='2asirtriana',db='mqtt')
	cursor = db.cursor()	
	query = "INSERT INTO data VALUES ('"+values+"');"	
	cursor.execute(query)
	db.commit()
	cursor.close() 	
	  
client = mqtt.Client()
client.connect("85.137.205.6",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
