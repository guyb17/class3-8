#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# Define global variables
password = getpass()

# Define dict for rtr1

pynet1 = {
     'device_type': 'cisco_ios', 
     'ip': '184.105.247.70',
     'username': 'pyclass',
     'password': password,
     'port': 22,
}	

pynet2 = {
     'device_type': 'cisco_ios',
     'ip': '184.105.247.71',
     'username': 'pyclass',
     'password': password,
     'port': 22,
}

pynet3 = {
     'device_type': 'juniper',
     'ip': '184.105.247.76',
     'username': 'pyclass',
     'password': password,
     'port': 22,
}

def main():
    pynet_rtr1 = ConnectHandler(**pynet1)
    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr3 = ConnectHandler(**pynet3)
#    output = pynet_rtr2.find_prompt()    
    print "Checking ARP Cache in RTR1"
    print  pynet_rtr1.send_command('sh arp')
    print "\n>>>"
    print "Checking ARP Cache in RTR2"
    print pynet_rtr2.send_command('sh arp')
    print "\n>>>"
    print "Checking ARP Cache in Juniper_SRX"
    print pynet_rtr3.send_command('sh arp')
#    output = pynet_rtr2.find_prompt()
#    print output

if __name__ == "__main__":
    main()

