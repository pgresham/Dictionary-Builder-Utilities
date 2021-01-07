#!/usr/bin/python3

import sys
try:
    infile = str(sys.argv[1])
    wordlength = int(sys.argv[2])
    outfile = str(sys.argv[3])
    f1 = open(infile,'r')
    f2 = open(outfile,'w')
    try:
        if str(sys.argv[4]) == 'upper':
            c = 2
        elif str(sys.argv[4]) == 'lower':
            c = 1
        elif str(sys.argv[4]) == 'pass':
            c = 0
        else:
            c = 0
    except:
        c = 0
    try:
        if str(sys.argv[5]) == 'nonames':
            n = 1
        else:
            n = 0
    except:
        n = 0
except:
    print('length_dictionary.py [input file] [word length] [output file] [lower|upper|pass] {nonames}')
    exit()   
if c == 0:
    if n == 1:
        for i in f1:
            if len(i.strip('\n')) == wordlength:
                if any(x.isupper() for x in i):
                    pass
                else:
                    f2.write(i)
            else:
                pass
    else:
        for i in f1:
            if len(i.strip('\n')) == wordlength:
                f2.write(i)
elif c == 1:
    if n == 1:
        for i in f1:
            if len(i.strip('\n')) == wordlength:
                if any(x.isupper() for x in i):
                    pass
                else:
                    f2.write(i.lower())
            else:
                pass
    else:
        for i in f1:
            if len(i.strip('\n')) == wordlength:
                f2.write(i.lower())
elif c == 2:
    if n == 1:
        for i in f1:
            if len(i.strip('\n')) == wordlength:
                if any(x.isupper() for x in i):
                    pass
                else:
                    f2.write(i.upper())
            else:
                pass
    else:
        for i in f1:
            if len(i.strip('\n')) == wordlength:
                f2.write(i.upper())

    
f1.close()
f2.close()

