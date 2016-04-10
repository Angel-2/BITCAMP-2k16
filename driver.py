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
from wifi_admin import Wifi_Admin_Scan

ASYNC_SCANS = [Sample_Scan(), Wifi_Type_Scan(), Mongo_Scan(), SSH_Scan(), FTP_Scan(), Telnet_Scan()]
SYNC_SCANS = [Wifi_Admin_Scan()]
def get_my_score(scan):
	print scan
	return scan.run_scan()


pool = Pool(processes=len(ASYNC_SCANS))
def get_total_scan_score():
	total = 0
	totals =  []
	synchronous_sum = 0
	for scan in ASYNC_SCANS:
		totals.append(pool.apply_async(get_my_score, args=(scan,)))
	for scan in SYNC_SCANS:
		print scan
		synchronous_sum += scan.run_scan()
	pool.close()
	pool.join()
	return (sum([total.get() for total in totals]) + synchronous_sum)/len(totals)