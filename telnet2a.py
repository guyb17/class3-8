#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_addr = 'x.y.z.70'
    username = 'uname'
    password = 'pword'
    test_command = 'show ip int brief'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    remote_conn.write(test_command + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()
