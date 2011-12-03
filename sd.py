import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "No arguments"
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                print sum([int(digit) for digit in line if digit.isdigit()])

    sys.exit(0)
