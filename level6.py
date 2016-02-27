#!/usr/bin/env python

import zipfile
import re

myzip = zipfile.ZipFile('./channel.zip', 'r')

bigdict = {}
for f in myzip.filelist:
    match = re.findall( r'\d+', f.filename)
    try:
        num = match[0]
        bigdict[num] = f.comment        
    except:
        break
    # myzip.open(f.filename).read()
    
num = '90052'
info = ''

while (True):
    filename = num + '.txt'
    info = info + bigdict[num]
    content = myzip.open(filename).read()
    # print content
    match = re.findall( r'\d+', content)
    try:
        num = match[0]
    except:
        break

print info