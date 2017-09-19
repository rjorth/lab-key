def new_gpa(points, credits):
    total_points = 0
    total_credits = 0
    new_entry = []
    cont = True

    while(cont):
        new_entry = raw_input("Please enter your points and credits ")
        
        points = new_entry[0]
        credits = new_entry[1]
        total_points += points
        totalCredits += credits
        if (new_entry = -1):
            cont = False
            
        gpa = total_points / total_credits
        print('Your gpa is: ' +str(gpa))
print('Program ends')
