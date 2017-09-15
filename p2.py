str = raw_input("Please enter a string:")
n = raw_input("Please enter a number:")
print(str *n) 
for i in range(1, n):
    print str[:-i]

if str == "-1" :
    print "end"

