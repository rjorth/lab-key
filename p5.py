#this problem is completed!
while True:
    word = raw_input('Please input a palindrome')
    word_rev = reversed(word)
    if list(word) == list(word_rev):
        print('Welcome to the Wonderland!')
        break
    else:
        print('No, you must input a palindrome')

