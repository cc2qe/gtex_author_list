#!/usr/bin/env python

import sys
import re

f = sys.stdin

aff_list = []
author_block = []

for line in f:
    if line.startswith('#'):
        if len(author_block) > 0:
            print ', '.join(author_block)
            print "" # blank line
            author_block = []
        
        print "##" + line.strip()
        continue

    v = line.rstrip('\n').split('\t')

    # clean up whitespace
    for i in xrange(len(v)):
        v[i] = re.sub("^ ", "", v[i])
        v[i] = re.sub(" $", "", v[i])
    
    first = v[0]
    middle = re.sub("\.", "", v[1]) # strip period
    last = v[2]
    author_aff = v[3:]

    # set name
    if middle == "":
        name = first + ' ' + last
    else:
        name = first + ' ' + middle + '. ' + last
    
    author_superscript = []
    
    for aff in author_aff:
        if aff == "": continue
        if aff not in aff_list:
            aff_list.append(aff)
        author_superscript.append(aff_list.index(aff)+1)

    author_superscript.sort()
    author_block.append(name + '<sup>' + ','.join(map(str, author_superscript)) + '</sup>')

print ', '.join(author_block)
print "" # blank line

for i in xrange(len(aff_list)):
    print str(i + 1) + '. ' + aff_list[i]

