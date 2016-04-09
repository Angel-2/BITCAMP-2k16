# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
import telnetlib

TELNET_PORT = '23'
TELNET_PORT_NUM = int(TELNET_PORT)

auths = [['', ''], ['admin', 'admin'], ['admin', 'password'], ['root', 'root'], ['root', 'password']] # blank auth is anon login

class Telnet_Scan:
    def run_scan(self):
        nm = nmap.PortScanner()
        nm.scan('192.168.0.1/16', TELNET_PORT) # scan everything on default telnet port
        for host in nm.all_hosts():
            if nm[host].has_tcp(TELNET_PORT_NUM) and nm[host]['tcp'][TELNET_PORT_NUM]['state'] == 'open':
                # for each host that's open on TELNET_PORT, try to connect
                # using each of the auth combos
                for auth in auths:
                    try:
                        conn = telnetlib.Telnet(host, TELNET_PORT_NUM)
                        return 0 # we only get here if ftp connected!
                    except:
                        continue
        return 100 # way hella
