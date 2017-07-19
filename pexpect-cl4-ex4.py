#!/usr/bin/env python

import pexpect
import time
from getpass import getpass


def main():
    username = 'pyclass'
    ip_addr = '184.105.247.71' 
    password = getpass()
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')

    ssh_conn.sendline(password)

    ssh_conn.expect('#')
    ssh_conn.send('\n')
    ssh_conn.expect('#')
#    time.sleep(0.5)  
    ssh_conn.sendline('config t')
#    time.sleep(0.5)
    ssh_conn.expect('#')
#    time.sleep(0.5)
    ssh_conn.sendline('logging buffered 9000')
#    time.sleep(0.5)
    ssh_conn.expect('#')
    print ssh_conn.before
#    time.sleep(0.5)
    ssh_conn.sendline('exit')
#    time.sleep(0.5)
    ssh_conn.expect('#')
    ssh_conn.sendline('sh run | i logging buff')
    ssh_conn.expect('#')
    print ssh_conn.before

if __name__ == "__main__":
    main()
