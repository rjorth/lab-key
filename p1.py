# 2.5.6
smallest = None

while True :
    firstNum = raw_input("Enter your first number:")
    if firstNum == "done" :
        break
    try :
        firstNum = int(firstNum)
    except :
        print "Invalid input"
        continue
    if smallest is None :
        smallest = firstNum
    elif firstNum < smallest :
        smallest = firstNum

print "The smallest number is", smallest
