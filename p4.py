playerOneNum = raw_input("Player 1, please write down your number secretly")
playerOneNum = int(playerOneNum)
notFound = True
count = 0

while notFound:
    count += 1
    playerTwoGuess = raw_input("Player2, please input your guess")
    playerTwoGuess = int(playerTwoGuess)
    if playerTwoGuess == playerOneNum:
        print "You are right after trying for", count, "times. Program ends."
        notFound = False
    elif playerTwoGuess > playerOneNum:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
