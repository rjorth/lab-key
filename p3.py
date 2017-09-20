notDone = True
points = 0
credits = 0

while notDone:
    gpa = raw_input("Input GPA and Credits:")
    try:
        val = int(gpa)
        if int(gpa) == -1:
            print("Program ends.")
            notDone = False
    except ValueError:
        gpa = str(gpa)
        gpa = gpa.split()
        point = float(gpa[0])
        credit = float(gpa[1])
        points += (point * credit)
        credits += credit
        GPA = (points/credits)
        print "Current GPA: ", GPA
