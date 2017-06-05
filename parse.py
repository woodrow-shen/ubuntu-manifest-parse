#!/usr/bin/python3

import os

list=""
with open('package.list', 'w') as pkg,  open('output.list', 'w') as out:
    with open('ubuntu.list', 'r', encoding='UTF-8') as file:
        for line in file:
            if ".deb" not in line:
                continue
            else:
                temp = line[:-1]
                list = list + "--include " +  os.path.basename(temp) + " "
                pkg.write(os.path.basename(line))
    list += '\n'
    out.write(list)
