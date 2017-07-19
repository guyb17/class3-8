#!/usr/bin/env python

import paramiko
import time

def disable_paging(remote_conn):
   remote_conn.send('terminal length 0\n')
   output = remote_conn.recv(64000)
   return output

ip = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
port = 22
#create SSH client object
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
print "SSH connected succesfully to %s" % ip


# Use invoke_shell to establish an interactive session for Cisco routers
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"

disable_paging(remote_conn)

remote_conn.send("\n")
remote_conn.send("show version\n")

time.sleep(5)

output = remote_conn.recv(3000)
print output


