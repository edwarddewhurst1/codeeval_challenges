import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "No arguments"
    else:
        with open(sys.argv[1], "r") as f:
            ints = []
            for line in f:
                ints.append(line)

            print sum([int(x) for x in ints])

    sys.exit(0)
