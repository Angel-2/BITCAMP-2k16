# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

from wifi import Cell, Scheme
from wifi.utils import match

wifi_ssid = "demowifi"
#wifi_ssid = "93848402743884848848485732010130"
interface = "wlan1"
filter = lambda cell : match(wifi_ssid, cell.ssid)


class Wifi_Type_Scan:
    def run_scan(self):
	scan = Cell.where(interface, filter)
	if(len(scan) > 0):
		network = scan[0]
		if(network.encrypted):
			if(network.encryption_type is 'wep'):
				return (10, "WEP Network Detected - Passwords can easily be hacked.")
			if(network.encryption_type is 'wpa'):
				return (20, "WPA Network Detected - Passwords may be vulnerable.")
			if(network.encryption_type is 'wpa2'):
				return (100, "Network encryption appears secure")
			else:
				return (100, "Network encryption apperas secure")
		else:
			return (0, "No network encryption")
