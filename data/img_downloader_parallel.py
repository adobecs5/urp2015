#!/usr/bin/env python

import multiprocessing as mp
import subprocess
import os
from bs4 import BeautifulSoup

limit = 1000
offset = 0
recovery = False

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
    a_HTML = l
    if recovery:
        b = os.path.getsize("html/%s.html" % l)
        if b > 0:
            print "skipping %d" % c
            return

    print "processing %d" % c
    with open("html/"+a_HTML+".html") as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        main_image_tag = soup.find(id = "imgTagWrapperId")
        img_url = main_image_tag.contents[1].attrs["src"]
        img_extension = img_url.split(".")[-1]
        for i in range(10):
            err = execute("wget %s -O html/images/%s.%s" % (img_url, a_HTML, img_extension))
            #print(err)
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

pool = mp.Pool()
lst = []

for i in range(offset):
    f.readline()

for i in range(limit):
    l = f.readline().strip()
    lst.append((l, i))
f.close()

pool.map(safe_run, lst)

