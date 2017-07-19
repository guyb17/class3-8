#!/usr/bin/env python

'''
script for logging into two routers and querying snmp oid objects
'''

import snmp_helper

Sys_Name = '1.3.6.1.2.1.1.5.0'
Sys_Descr =  '1.3.6.1.2.1.1.1.0'

def main():
	ip_addr1 = 'x.y.z.70'
        ip_addr2 = 'x.y.z.71'
        community = 'public'

        rtr1 = (ip_addr1, community, 161)
        rtr2 = (ip_addr2, community, 161)

        for rtr_x in (rtr1, rtr2):
           print "\n#####################"
           for the_oid in (Sys_Name, Sys_Descr):
               snmp_data = snmp_helper.snmp_get_oid(rtr_x, oid=the_oid)
               output = snmp_helper.snmp_extract(snmp_data)

           print output
        print "\##########################"

if __name__ == "__main__":
        main()
