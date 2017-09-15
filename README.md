# lab-key
#Exercise 1: The Smallest Number (20 marks)
raw_input() in Python 2 (equivalent to input() in Python 34) is a function that read
a string from a user’s input. The function can be used as raw_input([’prompt’]). For
example, after executing x = raw_input(’type a number:’) and reading the user typed
“one”, the variable x will store the string ”one”.
Write a script and save it as p1.py that will read four numeric values from the user’s
input. If the input is not a numeric value, then the user should be asked again to input
1An open data science platform powered by Python. https://www.continuum.io/downloads 2A powerful Python IDE. https://www.jetbrains.com/pycharm/download/ 3A non-CSE student should ask the TA for a CSDOMAIN account.
4Stackoverflow: What’s the dierence
between raw_input() and input() in python3.x?
1 of 4
CSCI 2040 Lab Assignment 1 Page 2
a numeric value and this round does not count. After that, print the smallest of the four
inputted values, print the line Program ends. and exit. A sample run should be as follows:
(Hint: use float() to convert a string to the corresponding numeric value)
Please input the first number: 10.15
Please input the second number: 33.2
Please input the third number: abc
Your input is not a number!
Please input the third number: 13.1
Please input the fourth number: -2.01
The smallest value is -2.01
Program ends.
If you use IDLE, you can test your script p1.py in the Python shell with
>>> execfile(’path/to/p1.py’)
Exercise 2: Pyramid of A String (20 marks)
Using while loop or for loop to write a script p2.py that reads an integer value n and a
string str from the user’s input and then produces an n-line block, repeatedly. For the n-line
output, the first line contains n strs, the second line contains n-1 ss, and so on until the n-th
line, which contains only one s. The script will keep asking the user to input an integer value
n and a string s and then print the corresponding n-line block. The script will print the line
Program ends. and exit if the user inputs an integer -1. For this exercise, you don’t need to
check whether the user’s input is an integer or not. A sample run should be as follows:
Enter an integer: 4
Enter a string:a
aaaa
aaa
aa
a
Enter an integer: 2
Enter a string:^_^
^_^^_^
^_^
Enter an integer: -1
Program ends.
Exercise 3: GPA Calculator (20 marks)
In order to improve GPA (Grade Point Average), the first thing at hand is to write a script
that calculate GPA quickly. With the script, a user could input the grade followed by the
2 of 4
CSCI 2040 Lab Assignment 1 Page 3
credit of a course. Immediately after reading the grade for a course, the GPA calculator print
out the current GPA. The user could keep adding the grades for more and more courses util
the user inputs -1. When the user inputs -1, the script will print the line Program ends.
and exit. The grade and credit are seperated by space. The GPA is NOT necessarily in
the format of 2 decimal points. (Hint: But you may use "0:.2f".format(a) if you want to
output 2 decimal points of a) A sample run shoud be as follows:
3.7 3
Current GPA: 3.70
3.3 2
Current GPA: 3.54
-1
Program ends.
Exercise 4: Guess My Number (20 marks)
Hint: To hide the input in Python, you could simply replace input() with getpass.getpass().
import getpass
getpass.getpass()
After knowing that the GPA is improved, the students want to play some games to relax.
They decide to play guess my number. Specifically, one of the player selects a integer in the
range [≠100, 100] and report it to the computer when seeing the prompt Player 1, write
down your number secretly:. After that, the script prompts another player for a guess
with the message Player 2, input your guess:. At each step, the script responds Your
guess is too low!, Your guess is too high! or You are right after trying for n
times. Program ends. Here n is the number of times that the user has tried to guess the
random integer correctly. A sample run should be like as follows,
Player 1, write down your number secretly:
Player 2, input your guess: 0
Your guess is too low!
Player 2, input your guess: 100
Your guess is too high!
Player 2, input your guess: 12
Your guess is too high!
Player 2, input your guess: 6
Your guess is too low!
Player 2, input your guess: 9
You are right after trying for 5 times. Program ends.
3 of 4
CSCI 2040 Lab Assignment 1 Page 4
Exercise 5: Palindrome Wonderland (20 marks)
In a secret place near the back hill of CUHK, there is a palindrome wonderland. People there
uses palindrome as their language. A palindrome is a string that reads the same backward
and forward. For example, the string eye and the string able was I ere I saw elba are
both palindromes. The palindrome wonderland has an entrance guard, which only allows the
people speaking palindrome to pass. You would implement such an entrance guard in p5.py.
The entrance guard start with the prompt Please input a string: that first reads a
string from the user’s input and check whether the input string is a palindrome or not and
the scripts would not exit until a palindrome is inputted. The script will print Welcome to
the wonderland! and the script exits if the input string is a palindrome. Otherwise, it
will print No. you must input a palindrome: and keep asking the user to input another
string if the input string is not a palindrome. (For this exercise, uppercase and lowercase
letters are treated as dierent
characters.) Hint: you can use raw_input() in Python 2 or
input() in Python 3. A sample run should be like as follows,
Please input a palindrome: 210
No, you must input a palindrome: 012
No, you must input a palindrome: 01210
Welcome to the wonderland!
