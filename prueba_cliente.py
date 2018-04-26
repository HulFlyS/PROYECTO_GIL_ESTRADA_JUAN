import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish

publish.single("paho/test/single", "boo", hostname="192.168.1.116:8080")
