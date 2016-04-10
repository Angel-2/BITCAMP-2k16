# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
import ftplib

FTP_PORT = '21'
FTP_PORT_NUM = int(FTP_PORT)

range = 'localhost'
DEFAULT_REPORT = "No FTP problems"

auths = [['', ''], ['admin', 'admin'], ['admin', 'password'], ['root', 'root'], ['root', 'password']] # blank auth is anon login

class FTP_Scan:
    def run_scan(self):
        score = 100
        report = ""
        
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
                        score -= 20
                        if score < 0:
                            score = 0
                        report += "\nFound FTP server with weak username and password (%s, %s) at address %s" % (auth[0], auth[1], host)
                    except:
                        continue
        return (score, report if score < 100 else DEFAULT_REPORT) # way hella
