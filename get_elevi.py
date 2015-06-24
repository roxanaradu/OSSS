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
        mingrade = 10
        maxgrade = 0
        for line in list(fp):
                line = line.strip()
                items = line.split('|')
                grade = int(items[3])
                if grade < mingrade:
                        mingr = grade
                        minpren = items[0]
                        minnume = items[1]
                        mingr = items[2]
                if grade > maxgrade:
                        maxgrade = grade
                        prenumemax = items[0]
                        numemax = items[1]
                        grupamax = items[2]
        print "MAX: %d, info student:  %s %s %s" % (maxgrade, prenumemax, numemax, grupamax)
        print "MIN: %d, info student: %s %s %s " % (mingr, minpren, minnume, mingr)

if __name__ == "__main__":
        sys.exit(main())
