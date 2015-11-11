#!/usr/bin/env python

import multiprocessing as mp
import subprocess
import os

limit = 1000
offset = 0
recovery = True

print "args: limit=%d, offset=%d" % (limit, offset)
if recovery:
    print "IN RECOVERY MODE"


def execute(line):
    p = subprocess.Popen(line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    status = p.wait()
    return err


def run(t):
    l, c = t

    if recovery:
        b = os.path.getsize("html/%s.html" % l)
        if b > 0:
            print "skipping %d" % c
            return

    print "processing %d" % c
    for i in range(10):
        err = execute("wget %s%s -O html/%s.html" % (url, l, l))
        if "200 OK" in err:
            return
        print "err: retry %s %d" % (l, c)
    print "fail: %s" % l


def safe_run(*args, **kwargs):
    try:
        run(*args, **kwargs)
    except Exception as e:
        print "error: %s run(*%r, **%r)" % (e, args, kwargs)


f = open('result.txt', 'r')
url = 'http://www.amazon.com/dp/'

pool = mp.Pool()
lst = []

for i in range(offset):
    f.readline()

for i in range(limit):
    l = f.readline().strip()
    lst.append((l, i))
f.close()

pool.map(safe_run, lst)

