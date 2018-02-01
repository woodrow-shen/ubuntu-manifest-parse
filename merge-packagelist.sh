#!/bin/sh

cat server-pool-arch.list desktop-pool-arch.list | sort -u > bionic-classic-arch.list
sed 's/\*_\(amd64\|all\).deb//g' bionic-classic-arch.list > bionic-classic-pkgname.list

./update-packagelist && cat udebs.list bionic-classic-apt.list > bionic-classic.list
