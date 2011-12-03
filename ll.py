from __future__ import print_function
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            lines = []
            for line in f:
                lines.append(line.strip('\n'))

            n = int(lines[0])
            lines.sort(key=len)
            lines = lines[::-1]
            for i in range(0, n):
                print(lines[i])

    sys.exit(0)

