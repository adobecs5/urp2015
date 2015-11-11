import json

f = open('clothes.json', 'r')
fw = open('result.txt', 'w')

cache = '0'
for l in f:
    d = json.loads(l)

    if cache != d['asin']:
        fw.write(d['asin'] + '\n')
        cache = d['asin']

f.close()
fw.close()
