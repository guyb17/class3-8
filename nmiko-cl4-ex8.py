#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
'''

from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler
from rtrs import pynet1, pynet2, juniper_srx

#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
'''
password = getpass()

    
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
        output = net_connect.config_mode("logging buffered 7000")
        print
        print '#' * 80
        print "Device: {}:{}".format(net_connect.ip, net_connect.port)
        print
        print output
        print '#' * 80
        print

    print "\nEnd time: " + str(datetime.now())

if __name__ == "__main__":
    main()


