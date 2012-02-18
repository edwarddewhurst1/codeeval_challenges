import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                n = ""
                for c in line:
                    if c != ",":
                        n += c



 
    sys.exit(0)
