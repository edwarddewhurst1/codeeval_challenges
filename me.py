from __future__ import print_function
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            lines = []
            for line in f:
                lines.append(line.strip("\n"))

            for line in lines:
                my_list = []
                for char in line:
                    if char != ' ':
                        my_list.append(char)
                n = int(str(my_list[-1:]).strip("[]'"))
                if n < len(my_list):
                    print(my_list[::-1][n])
    
    sys.exit(0)
