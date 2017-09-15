word = raw_input("Please input a palindrome")

word_rev = reversed(word)

def is_palindrome(word):
  if list(word) == list(word_rev):
    print'True, it is a palindrome'
  else:
    print'No, you must input a palindrome'

is_palindrome(word)
