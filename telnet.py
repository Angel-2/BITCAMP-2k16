# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

# import exp_runner
import nmap
import telnetlib

TELNET_PORT = '23'
TELNET_PORT_NUM = int(TELNET_PORT)
range = 'localhost'

auths = [['', ''], ['admin', 'admin'], ['admin', 'password'], ['root', 'root'], ['root', 'password']] # blank auth is anon login

class Telnet_Scan:
    def run_scan(self):
        nm = nmap.PortScanner()
        nm.scan(range, TELNET_PORT) # scan everything on default telnet port
        for host in nm.all_hosts():
            if nm[host].has_tcp(TELNET_PORT_NUM) and nm[host]['tcp'][TELNET_PORT_NUM]['state'] == 'open':
                # for each host that's open on TELNET_PORT, try to connect
                # using each of the auth combos
                for auth in auths:
                    try:
                        # should we also try to check for telnet servers
                        # that offer a shell without any attempt at auth?
                        conn = telnetlib.Telnet(host, TELNET_PORT_NUM)
                        conn.expect(["login: ", "Login: "], 5)
                        conn.write(auth[0] + "\r\n")
                        conn.expect(["Password: ", "password"], 5)
                        conn.write(auth[1] + "\r\n")
                        conn.write("\r\n")
                        (i, obj, res) = conn.expect(["Incorrect", "incorrect"], 5)
                        conn.close()

                        if i != -1: # auth failure
                            continue
                        else:
                            if any(map(lambda x: x in res, ["#", "$", ">"])) or len(res) > 500:
                                return 0
                    except:
                        continue
        return 100 # way hella
