#! /usr/bin/env python3

import paho.mqtt.client as mqtt
from converter import read_datagram
from serial_reader import read_telegram
from time import sleep
from json import dumps

power_topic = 'home/power_meter'
mqtt_server = '10.0.0.10'
client_name = 'power_meter'

def main():
    mqtt_client = mqtt.Client(client_name)
    mqtt_client.connect(mqtt_server, 1883)
    old_datagram = dict()
    for datagram in read_telegram():
        new_datagram = read_datagram(datagram)
        mqtt_client.publish(power_topic, dumps(new_datagram))
        sleep(5)


if __name__ == '__main__':
    main()
