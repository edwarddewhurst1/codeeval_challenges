import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "No arguments"
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                tmp = ""
                l = []
                for c in line:
                    if c == " " or c == "\n":
                        l.append(int(tmp))
                        tmp = ""
                    else:
                        tmp += c

                for i in range(1, len(l)):
                    if i % 2 != 0:
                        print l.pop(),
                    else:
                        l.pop()
                    

                print

    sys.exit(0)
