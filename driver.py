# main driver file
# register all scans here
# write functions to call them as appropriate
from multiprocessing.pool import Pool
from sample_scan import Sample_Scan
from wifi_type import Wifi_Type_Scan
from mongo import Mongo_Scan
from ssh import SSH_Scan
from ftp import FTP_Scan
from telnet import Telnet_Scan
from snort_scan import Snort_Scan
import time

ASYNC_SCANS = [Sample_Scan(), Wifi_Type_Scan(), Mongo_Scan(), SSH_Scan(), FTP_Scan(), Telnet_Scan()]

def get_my_score(scan):
	print "Now launching: "  + scan.name
	return scan.run_scan() + (scan.name, )


pool = Pool(processes=len(ASYNC_SCANS))
def get_total_scan_score():
	report = ""
	total = 0
	totals =  []
	scan_start = time.time()
	snorter = Snort_Scan()
	snorter.launch_scan() # we start early since it takes a while
	for scan in ASYNC_SCANS:
		totals.append(get_my_score(scan))


#Commented out for the demo but this reaches out to azure for snort analysis

	time.sleep(68 - (time.time() - scan_start))
	totals.append(snorter.run_scan())
	for scan in totals:
		subtotal = scan[0]
		subreport = scan[1]
		total += subtotal
		report += "\n%s" % subreport
	print report # TODO: actually return this
	return int(total / len(totals))
