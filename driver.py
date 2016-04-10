# main driver file
# register all scans here
# write functions to call them as appropriate
import re
from multiprocessing.pool import Pool
from sample_scan import Sample_Scan
from wifi_type import Wifi_Type_Scan
from mongo import Mongo_Scan
from ssh import SSH_Scan
from ftp import FTP_Scan
from telnet import Telnet_Scan

ASYNC_SCANS = [Sample_Scan(), Wifi_Type_Scan(), Mongo_Scan(), SSH_Scan(), FTP_Scan(), Telnet_Scan()]
# SYNC_SCANS = [Wifi_Admin_Scan()]
REPORT_FILE = 'report.html'

def get_my_score(scan):
	print scan
	return scan.run_scan()


pool = Pool(processes=len(ASYNC_SCANS))
def get_total_scan_score():
	report = ""
	total = 0
	totals =  []
	synchronous_sum = []
	for scan in ASYNC_SCANS:
		print scan
		totals.append(get_my_score(scan))
	for scan in totals:
		print totals
		subtotal = scan[0]
		subreport = scan[1]
		total += subtotal
		print subtotal
		report += "\n%s" % subreport
	#print report # TODO: actually return this
        report = "</p>\n<p>".join(report.split("\n"))
        report = "<html>\n<p>%s</p>\n</html>" % report
        with open(REPORT_FILE, 'w') as report_file:
                report_file.write(report)
	return int(total / len(totals))
