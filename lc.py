#!/usr/bin/env python
from __future__ import print_function
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No argument")
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
               print(line.lower(), end="")

    sys.exit(0)
