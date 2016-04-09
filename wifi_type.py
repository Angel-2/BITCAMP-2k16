# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

from wifi import Cell, Scheme
from wifi.utils import match

wifi_ssid = "EventWifi 2.4ghz"
#wifi_ssid = "93848402743884848848485732010130"
interface = "wlan0"
filter = lambda cell : match(wifi_ssid, cell.ssid)


class Wifi_Type_Scan:
    def run_scan(self):
	scan = Cell.where(interface, filter)
	if(len(scan) > 0):
		network = scan[0]
		if(network.encrypted):
			if(network.encryption_type is 'wep'):
				return 10
			if(network.encryption_type is 'wpa'):
				return 20
			if(network.encryption_type is 'wpa2'):
				return 100
			else:
				return 100
		else:
			return 0
