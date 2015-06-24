#!/usr/bin/env python

import sys


def usage():
        print >> sys.stderr, "Usage: python %s  <filename> " % (sys.argv[0])


def main():
        if len(sys.argv) != 2:
                usage()
                sys.exit(1)
        try:
                fp = open(sys.argv[1], "r")
        except IOError, e:
                print >> sys.stderr, "Argument is not a valid filename"
                usage()
                sys.exit(1)
        mingrade=10
        maxgrade=0        
        
        for line in list(fp):
                #print "linia curenta este %s" %(line)
                line=line.strip()
                items=line.split('|')
                grade=int(items[3])
                if grade<mingrade:
                        mingrade=grade
                        prenumemin=items[0]
                        numemin=items[1]
                        grupamin=items[2]
                if grade>maxgrade:
                        maxgrade=grade
                        prenumemax=items[0]
                        numemax=items[1]
                        grupamax=items[2]
        print "Nota maxima este %d iar info student:  %s %s %s" %(maxgrade,prenumemax,numemax,grupamax)
        print "Nota miima este %d iar info student: %s %s %s " %(mingrade,prenumemin,numemin,grupamin)

if __name__ == "__main__":
        sys.exit(main())

