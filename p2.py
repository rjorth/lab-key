#needed edits: program ends when -1 is entered. 
while True:
    str = raw_input("Please enter a string:")
    n = int(raw_input("Please enter a number:"))
    while n > 0:
        print (str * int(n))
        n -= 1
    

