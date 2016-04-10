# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
import spur

SSH_PORT = '22'
SSH_PORT_NUM = int(SSH_PORT)
DEFAULT_REPORT = "No problems with SSH"

auths = [['admin', 'admin'], ['admin', 'password'], ['root', 'root'], ['root', 'password']]
range = '192.168.*'

class SSH_Scan:
    def run_scan(self):
        score = 100
        report = ""
        
        nm = nmap.PortScanner()
        nm.scan(range, arguments='--open -T5 -p '+ str(SSH_PORT)) # scan everything on default ssh port
        for host in nm.all_hosts():
            if nm[host].has_tcp(SSH_PORT_NUM) and nm[host]['tcp'][SSH_PORT_NUM]['state'] == 'open':
                # for each host that's open on SSH_PORT, try to connect
                # using each of the auth combos
                for auth in auths:
                    shell = spur.SshShell(hostname = host, username = auth[0], password = auth[1], missing_host_key = spur.ssh.MissingHostKey.accept)
                    try:
                        result = shell.run(['ls'])
                        score -= 50 # we only get here if the ssh connected!
                        if score < 0:
                            score = 0
                        report += "\nVulernable SSH server with username and password (%s, %s) found at address %s" % (auth[0], auth[1], host)
                    except:
                        continue
        return (score, report if score < 100 else DEFAULT_REPORT) # way hella
