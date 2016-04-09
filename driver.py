# main driver file
# register all scans here
# write functions to call them as appropriate

from sample_scan import Sample_Scan

SCANS = [Sample_Scan()]

def get_total_scan_score():
    total = 0
    for scan in SCANS:
        total += scan.run_scan()
    return total
