import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                i = 0
                line = line.strip(' \n')
                while line != line[::-1]:
                    line = str(int(line) + int(line[::-1]))
                    i += 1

                print "%i %s" % (i, line)

    sys.exit(0)
