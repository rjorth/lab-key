# 2.5.6
number1 = int(raw_input('Enter First number : '))
number2 = int(raw_input('Enter Second number : '))
number3 = int(raw_input('Enter Third number : '))
number4 = int(raw_input('Enter Fourth number: '))
def smallest(num1, num2, num3, num4):
    if (num1 < num2) and (num1 < num3) and (num1 < num4):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3) and (num2 < num4):
        smallest_num = num2
    elif (num3 < num1) and (num3 < num2) and (num3 < num4):
          smallest_num = num3
    else:
      		smallest_num = num4
    print('The smallest of the numbers is : ', smallest_num)
smallest(number1, number2, number3, number4)
#still need to create the prompt for 'invalid input' that does not disrupt the program. 
