# each scan must implement a run_scan() method
# which returns a value from 0 to 100, inclusive
# 100 is the best score, 0 is the worst

class Sample_Scan:
    name = "Test Scan"
    def run_scan(self):
        return (100, "No problems with the test scan plugin.") # way hella
