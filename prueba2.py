import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

mqttc.connect("192.168.1.116:1883")
#mqttc.loop_start()

#while True:
#    temperature = sensor.blocking_read()
#    mqttc.publish("paho/temperature", temperature)
