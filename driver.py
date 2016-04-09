# main driver file
# register all scans here
# write functions to call them as appropriate

from sample_scan import Sample_Scan
from wifi_type import Wifi_Type_Scan
from mongo import Mongo_Scan
from ssh import SSH_Scan
from ftp import FTP_Scan
from telnet import Telnet_Scan

from wifi_admin import Wifi_Admin_Scan

SCANS = [Sample_Scan(), Wifi_Type_Scan(), Wifi_Admin_Scan(), Mongo_Scan(), SSH_Scan(), FTP_Scan(), Telnet_Scan()]

def get_total_scan_score():
    total = 0
    for scan in SCANS:
        total += scan.run_scan()
    return total
