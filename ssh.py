# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
import spur

SSH_PORT = '22'
SSH_PORT_NUM = int(SSH_PORT)

auths = [['admin', 'admin'], ['admin', 'password'], ['root', 'root'], ['root', 'password']]

class SSH_Scan:
    def run_scan(self):
        nm = nmap.PortScanner()
        nm.scan('192.168.0.1/16', SSH_PORT) # scan everything on default ssh port
        for host in nm.all_hosts():
            if nm[host].has_tcp(SSH_PORT_NUM) and nm[host]['tcp'][SSH_PORT_NUM]['state'] == 'open':
                # for each host that's open on SSH_PORT, try to connect
                # using each of the auth combos
                for auth in auths:
                    shell = spur.SshShell(hostname = host, username = auth[0], password = auth[1], missing_host_key = spur.ssh.MissingHostKey.accept)
                    try:
                        result = shell.run(['ls'])
                        return 0 # we only get here if the ssh connected!
                    except:
                        continue
        return 100 # way hella
