#!/usr/bin/env python

from time import sleep
import subprocess

def execute(line):
    p = subprocess.Popen(line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    status = p.wait()
    return err


f = open('result.txt', 'r')
ff = open('fail.txt', 'w')
url = 'http://www.amazon.com/dp/'

count = 0
for l in f:
    l = l.strip()
    for i in range(10):
        err = execute("wget %s%s -O html/%s.html" % (url, l, l))
        if "200 OK" in err:
            break

    if i == 9:
        ff.write(l + '\n')

    count += 1
    print count
    if count == 1000:
        break

f.close()
ff.close()
