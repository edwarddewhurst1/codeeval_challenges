#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("No argument")
else:
    with open(sys.argv[1], "r") as f:
        for line in f:
            index = 0
            values = ["","",""]
            for c in line:
                if c.isdigit():
                    values[index] += c
                elif not c.isalpha() and index < 4:
                    index += 1

            val1 = int(values[0])
            val2 = int(values[1])
            rng = int(values[2]) + 1
            result = ""
            
            for i in range(1, rng):
                if i % val1 == 0 and i % val2 == 0:
                    result += "FB "
                elif i % val1 == 0:
                    result += "F "
                elif i % val2 == 0:
                    result += "B "
                else:
                    result += str(i) + " "

            print(result)


sys.exit(0)
