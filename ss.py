import sys
import re

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments")
    else:
        with open(sys.argv[1], "r") as f:
            for line in f:
                after_comma = False
                string = ""
                sub_string = ""
                for c in line:
                    if c != ',' and after_comma == False:
                        string += c
                    elif c != ',' and after_comma == True:      
                        sub_string += c
                    elif c == ',':
                        after_comma = True
                sub_string = sub_string.strip(' \n')
                sub_string = r"%s" % sub_string
                match = re.search(sub_string, string)
                
                if match:
                    print "true"
                else:
                    print "false"                

    sys.exit(0)
