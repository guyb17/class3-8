#!/usr/bin/env python

import snmp_helper

IP = 'x.y.v.z'
a_user = 'pysnmp'
auth_key = 'key'
encryp_key = 'encrypt'
snmp_user = (a_user, auth_key, encryp_key,)
pynet_rtr2 = (IP, 161)

snmp_oids = (
	('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
	('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
	('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
	('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
	('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

for desc,an_oid,count_is  in snmp_oids:
  snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=an_oid)
  output = snmp_helper.snmp_extract(snmp_data)
  print "%s %s" % (desc, output)

