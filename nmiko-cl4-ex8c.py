#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
'''

from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler
from rtrs import pynet1, pynet2

#!/usr/bin/env python
'''
Use Netmiko to execute 'logging buffered <7000>' and 'no logging console' on pynet-rtr1, pynet-rtr2
'''
password = getpass()

config_commands = ['logging buffered 7000', 'no logging console']

    
def main():
    '''
    Use Netmiko to execute 'logging bufferd <size>' and 'no logging console' on pynet-rtr1 and pynet-rtr2)
    '''
#    password = getpass()

    # Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2):
        a_dict['password'] = password
        a_dict['verbose'] = False

    print "\nStart time: " + str(datetime.now())
    for a_device in (pynet1, pynet2):
        net_connect = ConnectHandler(**a_device)
        net_connect.send_config_set(config_commands)
        output = net_connect.send_config_set(config_commands)

        print
        print '#' * 80
        print "Device: {}:{}".format(net_connect.ip, net_connect.port)
        print output
        print "show run | i logging output:\n" + net_connect.send_command('show run | i logging')
        print '#' * 80

    print "\nEnd time: " + str(datetime.now())

if __name__ == "__main__":
    main()


