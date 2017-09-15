str = raw_input("Please enter a string:")
n = raw_input("Please enter a number:")

for n in range(1, len(str)):
    print str[:-n]

if str == "-1" :
    print "end"

