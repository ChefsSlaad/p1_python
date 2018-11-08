#!/usr/bin/python3
import paho.mqtt.client as mqtt
from converter import read_datagram
from serial_reader import read_telegram

power_topic = "home/power_meter"
mqtt_server = '10.0.0.10'
client_name = 'power_meter'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect(mqtt_server, 1883)

old_datagram = dict()
for datagram in read_telegram():
#    print(datagram)
#    print(datagram.splitlines())

    new_datagram = read_datagram(datagram)
    dif_datagram = dict(new_datagram.items() - old_datagram.items())
    old_datagram = new_datagram
    print(dif_datagram)
#    print(new_datagram)
