#! /home/eliadcohen/projects/AnsiblePlaybooks/venv/bin/python
from __future__ import print_function
import sys
import libvirt


domName = 'rhel7ANS1'
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

stats="ACTIVE" if dom.isActive()==1 else "Inactive"
print('Uptime:\n'+stats)

conn.close()
exit(0)