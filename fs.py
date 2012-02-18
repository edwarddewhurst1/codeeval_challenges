#!/usr/bin/env python
import sys, os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "No arguments"
    else:
        print(os.path.getsize(sys.argv[1]))    

    sys.exit(0)
