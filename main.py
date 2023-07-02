def is_palindrome(word):
  """
  This function takes a string as input and returns True if the string is a palindrome, False otherwise.

  Args:
    word: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  word = word.replace(' ', '')
  reversed_word = word[::-1]

  return word == reversed_word


if __name__ == '__main__':
  word = input('Enter a word or phrase: ')

  if is_palindrome(word):
    print(f'{word} is a palindrome')
  else:
    print(f'{word} is not a palindrome')
