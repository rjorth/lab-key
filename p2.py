#this problem is completed but definitely not in the usual way. 
notDone = True
while notDone:
    n = int(raw_input('Please enter a number: '))
    try:
        val = int(n)
        if int(n) == -1:
            print('Program ends.')
            notDone = False
    except ValueError:
        print(str * int(n))
        n -= 1

    while n>0:
        str = raw_input('Please enter a string: ')
        while n>0:
            print(str * int(n))
            n -= 1

