#!/usr/bin/env python
import sys

def primes_less_than(n):
    l = [x for x in range(2, n)]
    i = 0
    marked = []

    while True:
        p = l[i]
        tmp = l[i::p][1:]
        if len(tmp) > 0:
            for x in tmp:
                marked.append(x)
            i += 1
        else:
            break
    
    for x in marked:
        try:
            l.remove(x)
        except ValueError:
            pass

    return l

ARGV = sys.argv

if __name__ == "__main__":
    if len(ARGV) < 2:
        print "Usage: %s <input file>" % ARGV[0]
    else:
        with open(ARGV[1], "r") as f:
            for line in f:
                answer = str(primes_less_than(int(line.strip('\n '))))
                print answer.replace(' ', '').strip("[]")
    sys.exit(0)
