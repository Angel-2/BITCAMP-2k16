# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst
import subprocess
import time
import requests
import json

class Snort_Scan:


    name = "Snort Alert Detected"
    def launch_scan(self):
        subp = subprocess.Popen(["sudo ./capture.sh"], shell=True)


    def run_scan(self):
        try:
            if 'classtype' in open('snort_results.txt'):
                return (10, "Our snort server detected suspicous activity on your network that may be indicative of malware.")
            else:
                return (100, "No malware detected on network.") # way hella
        except:
                return (100, "No malware detected on network.")
