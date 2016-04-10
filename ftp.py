# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
import ftplib

FTP_PORT = '21'
FTP_PORT_NUM = int(FTP_PORT)
range = 'localhost'

auths = [['', ''], ['admin', 'admin'], ['admin', 'password'], ['root', 'root'], ['root', 'password']] # blank auth is anon login

class FTP_Scan:
    def run_scan(self):
        nm = nmap.PortScanner()
        nm.scan(range, FTP_PORT) # scan everything on default ftp port
        for host in nm.all_hosts():
            if nm[host].has_tcp(FTP_PORT_NUM) and nm[host]['tcp'][FTP_PORT_NUM]['state'] == 'open':
                # for each host that's open on FTP_PORT, try to connect
                # using each of the auth combos
                for auth in auths:
                    try:
                        conn = ftplib.FTP(host)
                        conn.login(auth[0], auth[1])
                        return 0 # we only get here if ftp connected!
                    except:
                        continue
        return 100 # way hella
