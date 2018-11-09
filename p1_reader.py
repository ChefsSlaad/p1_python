#! /usr/bin/env python3

import paho.mqtt.client as mqtt
from converter import read_datagram
from serial_reader import read_telegram
from time import sleep, time
from json import dumps

power_topic = 'home/power_meter'
mqtt_server = '10.0.0.10'
client_name = 'power_meter'
refresh_int = 15

def main():
    secs = time()
    mqtt_client = mqtt.Client(client_name)
    mqtt_client.connect(mqtt_server, 1883)
    gas_old = 0
    pwr_old = 0
    max_time = 0
    for telegram in read_telegram():
        datagram = read_datagram(telegram)
#        print('t1', datagram['tarif_1_delivered'], 't2', datagram['tarif_2_delivered'])

        if time()-secs > max_time: 
#            print()
            pwr = datagram['tarif_1_delivered'] + datagram['tarif_2_delivered']
            pwr_avg= round((pwr - pwr_old)*(3600000/refresh_int),3)
            datagram['power_avg'] = pwr_avg

            gas = datagram['gas_delivered']
            gas_avg = round((gas - gas_old)*(3600000/refresh_int),3)
            datagram['gas_avg'] = gas_avg
#            print('{:3} current_power {:10} last_power {:10} diff {}'.format(round(time()-secs), pwr  , pwr_old, pwr_avg))
#            print('{:3} current gas   {:10} last gas   {:10} diff {}'.format(round(time()-secs),gas, gas_old, gas_avg))
#            print(round(time()-secs), 'gas', gas_avg, 'power', pwr_avg)
            if max_time > 0:
                mqtt_client.publish(power_topic, dumps(datagram))
                for k, v in datagram.items():
                    print('{:20} - {}'.format(k,v))
            gas_old = gas
            pwr_old = pwr
            secs = time()
            max_time = refresh_int
        sleep(1)

if __name__ == '__main__':
    main()
