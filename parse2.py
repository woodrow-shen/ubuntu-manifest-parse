#!/usr/bin/python3

import os
import apt

with open('package.list', 'w') as out:
    with open('xlist', 'r', encoding='UTF-8') as file:
        for line in file:
            cache = apt.Cache()
            temp = line[:-1]
            try:
                apt_pkg = cache[temp]
                ver = apt_pkg.versions
                pkg_info = str(ver[0]).split('=')
                print(pkg_info)
                if ":" not in pkg_info[1]:
                    pkg_name = pkg_info[0] + '_' + pkg_info[1] + '_*.deb'
                else:
                    pkg_name = pkg_info[0] + '_' + pkg_info[1].split(':')[1] + '_*.deb'
            except KeyError as err:
                print("KeyError %s" % format(err))
                pkg_name = temp + '*.udeb'
                out.write(pkg_name + '\n')
            else:
                out.write(pkg_name + '\n')
