#!/usr/bin/env python
# encoding: utf-8

import subprocess

#command 1          //这段代码是查询系统信息的
uname = "uname"
uname_arg = "-a"
print "gathering system information with $s command:\n" % uname
subprocess.call([uname,uname_arg])

#command 2       //这段代码是查询磁盘分区使用情况的
diskspace = "df"
diskspace_arg = "-h"
print "gathering diskspace information %s command:\n"  %  diskspace
subprocess.call([diskspace,diskspace_arg])
