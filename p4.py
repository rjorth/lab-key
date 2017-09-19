import getpass
getpass.getpass("Player1, please enter your number")


for i in range(0,20):
    player2 = raw_input("Player2, please input your guess")
    if player2 !== getpass:
        print("Try again")
        continue
    else: 
        print("You are right") 
# alternative attempt
import getpass
player1 = getpass.getpass('Player1, please enter your number: ')

for player2 in range(0,5):
    player2 = raw_input('Player 2, please input your guess')
    if player2 == player1:
        print('You are correct!')
        break
    elif player2 != player1 :
        print('You are not correct.')
        continue
    else:
        print('You are correct after 5 guesses.')
        break
