import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "No arguments"
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                ue = set()
                for c in line:
                    if c.isdigit():
                        ue.add(int(c))

                print str(sorted(ue)).strip('[]')

    sys.exit(0)
