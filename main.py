import wifi_config
from machine import UART


wifi_config.scan_and_connect(networks = ({'ssid': 'home', 'password':'Garuda180'}))


uart0 = UART(0, 115200)
#uart1 = UART(1)
uart0.init(115200, parity = None, bits = 8, stop = 0)
#uart1.init(115200, parity = None, bits = 8, stop = 0)
