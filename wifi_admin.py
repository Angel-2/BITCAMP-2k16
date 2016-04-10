# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst
import routersploit.wordlists as wordlists
import netifaces
import requests
import nmap
from multiprocessing.pool import Pool
import routersploit.modules.creds.ftp_default as ftp_scan
import routersploit.modules.creds.http_form_default as http_scan
import routersploit.modules.creds.ssh_default as ssh_scan
import routersploit.modules.creds.telnet_default as telnet_scan

def get_default_gateway():
	return netifaces.gateways()['default'][netifaces.AF_INET][0]	


class Wifi_Admin_Scan:

    threader = Pool(processes=5)

    def brute_scanner(module):
        brute = module.Exploit()
        brute.target = get_default_gateway()
        brute.usernames = wordlists.usernames
        brute.passwords = wordlists.passwords
        try:
            return brute.run()
        except:
            print "error"
            return (0)

    def run_scan(self):
        scores = []
        gateway = get_default_gateway()
        if len(gateway) > 0:
            nm = nmap.PortScanner()
            nm.scan(gateway, '21, 22, 23, 80')

            if(nm[gateway].has_tcp('21')):
                scores.append(self.threader.apply_async(ftp_scan))
            if(nm[gateway].has_tcp('22')):
                scores.append(self.threader.apply_async(ssh_scan))
            if(nm[gateway].has_tcp('23')):
                scores.append(self.threader.apply_async(telnet_scan))
            if(nm[gateway]).has_tcp('80'):
                scores.append(self.threader.apply_async(http_scan))

            self.threader.close()
            self.threader.join()
            return 100 # way hella

scan = Wifi_Admin_Scan().run_scan()