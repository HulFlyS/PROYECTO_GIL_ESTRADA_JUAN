#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import random
import commands

client = mqtt.Client()
client.connect("85.137.205.6",1883,60)
client.publish("topic/num", random.randint(0, 200));
client.publish("topic/name", commands.getoutput('hostname'));
client.publish("topic/date", commands.getoutput('date'));
client.disconnect();
