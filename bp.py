import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                stage = 0
                n = p1 = p2 = ""
                for c in line:
                    if c != ',' and stage == 0:
                        n += c
                    elif c != ',' and stage == 1:
                        p1 += c
                    elif c != ',' and stage == 2:
                        p2 += c
                    elif c == ',':
                        stage += 1

                p2 = p2.strip(' \n')

                n = bin(int(n))[2:][::-1]
                p1 = int(p1) - 1
                p2 = int(p2) - 1

                if n[p1] == n[p2]:
                    print "true"
                else:
                    print "false"

    sys.exit(0)
