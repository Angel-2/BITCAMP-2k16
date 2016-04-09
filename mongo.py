# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
from pymongo import MongoClient

MONGO_PORT = '27017'
MONGO_PORT_NUM = int(MONGO_PORT)

class Mongo_Scan:
    def run_scan(self):
        nm = nmap.PortScanner()
        nm.scan('192.168.0.1/16', MONGO_PORT) # scan everything on default mongo port
        for host in nm.all_hosts():
            if nm[host].has_tcp(MONGO_PORT_NUM) and nm[host]['tcp'][MONGO_PORT_NUM]['state'] == 'open':
              # for each host that's open on MONGO_PORT, try to connect
              client = MongoClient(host, MONGO_PORT_NUM)
              if client.nodes() == frozenset([]): # no connection
                  client.close()
                  continue
              else: # connection!
                  return 0
        return 100 # way hella
