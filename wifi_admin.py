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

    name = "Wifi Access Scan"

    def brute_scanner(self, module):
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
        threader = Pool(processes=5)
        scores = []
        gateway = get_default_gateway()
        score_list = []
        if len(gateway) > 0:
            nm = nmap.PortScanner()
            nm.scan(hosts=gateway, ports="21,22,23,80", arguments='-sV -T5')

            if nm[gateway].has_tcp(21):
                scores.append(self.brute_scanner(ftp_scan))
            if nm[gateway].has_tcp(22):
                scores.append(self.brute_scanner(ssh_scan))
           # if nm[gateway].has_tcp(23):
           #     scores.append(self.brute_scanner(telnet_scan))
            if nm[gateway].has_tcp(80):
                scores.append(self.brute_scanner(http_scan))
            if nm[gateway].has_tcp(21) or nm[gateway].has_tcp(22) or nm[gateway].has_tcp(23) or nm[gateway].has_tcp(80) or len(scores) < 1:
                score = int(sum([score[0] for score in scores])/scores)
                response = "".join([score[1] for score in scores])
                return (score, response)
            else:
                return (100, "No router login issues.")
