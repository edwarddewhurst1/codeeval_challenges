import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                print sum([int(x) for x in bin(int(line))[2:]]) / 1
                

    sys.exit(0)

