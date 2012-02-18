from __future__ import print_function
import sys

if len(sys.argv) < 2:
    print("No args.")
else:
    with open(sys.argv[1], "r") as f:
        for line in f:
            tmp = ""
            words = []
            for c in line:
                if c.isalpha():
                    tmp += c
                else:
                    words.append(tmp)
                    tmp = ""

            words.reverse()
            for word in words:
                print(word, end=' ')

            print()

sys.exit(0)
