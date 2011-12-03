import sys

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a+b
        count += 1

    return a

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "No arguments"
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                num = ""
                for c in line:
                    if c == '\n':
                        break    
                    else:
                        num += c
                print fibonacci(int(num))

    sys.exit(0)
