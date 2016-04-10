# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst
import subprocess
import time

class Sample_Scan:


    name = "Snort Alert Detected"
    def run_scan(self):
        subp = subprocess.Popen(["snort -c /etc/snort/snort.conf -i wlan1 -A fast -q > result_scan.txt"], shell=True)
        time.sleep(30)
        print "test"

        return (100, "No problems with the test scan plugin.") # way hella



testScan = Sample_Scan()

testScan.run_scan()

