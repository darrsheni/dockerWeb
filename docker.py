#!/usr/bin/python3
print("content-type:text/html")
print()

import cgi
import subprocess
ret=cgi.FieldStorage()
cmd=ret.getValue("x")
d=subprocess.getoutput("sudo " +cmd)
print(d)

