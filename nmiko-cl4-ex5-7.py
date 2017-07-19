#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# Define global variables
password = getpass()

# Define dict for rtr1

pynet2 = {
     'device_type': 'cisco_ios', 
     'ip': '184.105.247.71',
     'username': 'pyclass',
     'password': password,
     'port': 22,
}	

def main():
    pynet_rtr2 = ConnectHandler(**pynet2)
#    output = pynet_rtr2.find_prompt()    
    pynet_rtr2.config_mode()
    pynet_rtr2.send_command('logging buffered 7000')
    print pynet_rtr2.check_config_mode()
    output = pynet_rtr2.find_prompt()
    print output

    pynet_rtr2.exit_config_mode()
    output = pynet_rtr2.send_command('sh run | i logging buffer')
    print output

if __name__ == "__main__":
    main()

