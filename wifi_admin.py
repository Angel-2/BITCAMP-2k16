# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import netifaces
import requests

def get_default_gateway():
	return netifaces.gateways()['default'][netifaces.AF_INET][0]	

class Wifi_Admin_Scan:
    def run_scan(self):
	gateway = get_default_gateway()
	if(len(gateway) > 0):
		r = requests.get('http://' + gateway, verify=False)
		print r.status_code
        return 100 # way hella
