#!/usr/bin/python3

import os
import sys
import apt

linux_package = [
"block-modules",
"crypto-modules",
"dasd-extra-modules",
"dasd-modules",
"fat-modules",
"fb-modules",
"firewire-core-modules",
"floppy-modules",
"fs-core-modules",
"fs-secondary-modules",
"input-modules",
"ipmi-modules",
"irda-modules",
"kernel-image",
"linux-cloud-tools",
"linux-cloud-tools-common",
"linux-doc",
"linux-headers",
"linux-image",
"linux-image-extra",
"linux-libc-dev",
"linux-source",
"linux-tools",
"linux-tools-common",
"linux-udebs-generic",
"linux-udebs-generic-lpae",
"md-modules",
"message-modules",
"mouse-modules",
"multipath-modules",
"nfs-modules",
"nic-modules",
"nic-pcmcia-modules",
"nic-shared-modules",
"nic-usb-modules",
"parport-modules",
"pata-modules",
"pcmcia-modules",
"pcmcia-storage-modules",
"plip-modules",
"ppp-modules",
"sata-modules",
"scsi-modules",
"serial-modules",
"storage-core-modules",
"usb-modules",
"virtio-modules",
"vlan-modules",
"kernel-signed-image",
"linux-signed-image"
]

with open('package.list', 'w') as out:
    with open('input.list', 'r', encoding='UTF-8') as file:
        for line in file:
            cache = apt.Cache()
            temp = line[:-1]
            if ".deb" in line:
                try:
                    #print(temp.split('*'))
                    pkg_name = temp.split('*')
                    apt_pkg = cache[pkg_name[0]]
                    ver = apt_pkg.versions
                    pkg_info = str(ver[0]).split('=')
                    #print(pkg_info)
                    if ":" not in pkg_info[1]:
                        pkg_file = pkg_info[0] + '_' + pkg_info[1] + pkg_name[1]
                    else:
                        pkg_file = pkg_info[0] + '_' + pkg_info[1].split(':')[1] + pkg_name[1]
                    out.write(pkg_file + '\n')
                except KeyError as err:
                    print("KeyError %s" % format(err))
                    out.write(line)
            else:
                out.write(line)
