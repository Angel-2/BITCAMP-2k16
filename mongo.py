# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

import nmap
from pymongo import MongoClient

MONGO_PORT = '27017'
MONGO_PORT_NUM = int(MONGO_PORT)
range = '192.168.*'
DEFAULT_REPORT = "No problems with MongoDB"

class Mongo_Scan:

    name = "Mongo DB Vulnerability Scanner"

    def run_scan(self):
        score = 100
        report = ""
        
        nm = nmap.PortScanner()
        nm.scan(range, MONGO_PORT, arguments="-sV -T5") # scan everything on default mongo port
        for host in nm.all_hosts():
            if nm[host].has_tcp(MONGO_PORT_NUM) and nm[host]['tcp'][MONGO_PORT_NUM]['state'] == 'open':
              # for each host that's open on MONGO_PORT, try to connect
              client = MongoClient(host, MONGO_PORT_NUM)
              if client.nodes() == frozenset([]): # no connection
                  client.close()
                  continue
              else: # connection!
                  score -= 50
                  if score < 0:
                      score = 0
                  report += "\nVulnerable MongoDB server found at address %s" % (host)
        return (score, report if score < 100 else DEFAULT_REPORT) # way hella
