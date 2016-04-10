# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

from wifi import Cell, Scheme
from wifi.utils import match

wifi_ssid = "EventWifi 2.4ghz"
#wifi_ssid = "93848402743884848848485732010130"
interface = "wlan0"
filter = lambda cell : match(wifi_ssid, cell.ssid)

DEFAULT_REPORT = "No problems with the WiFi type"

class Wifi_Type_Scan:
    def run_scan(self):
        score = 100
        report = ""
        
	scan = Cell.where(interface, filter)
	if(len(scan) > 0):
		network = scan[0]
		if(network.encrypted):
			if(network.encryption_type is 'wep'):
				score = 10
                                report = "Vulnerable (WEP) network found"
			if(network.encryption_type is 'wpa'):
				score = 20
                                report = "Vulnerable (WPA) network found"
			if(network.encryption_type is 'wpa2'):
                                score = 100
			else:
				score = 100
		else:
			score = 0
                        report = "Highly vulnerable unsecured network found"
        return (score, report if score < 100 else DEFAULT_REPORT)
