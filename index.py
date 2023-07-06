'''
Question 1
Write a function that takes in a sentence and returns the 3 most common letters. 
Spaces should not be counted as letters.
Raise a custom exception when this function wouldn’t be able to return 3 common
letters.
Question 2
Write unit tests for the previous function. Make sure it covers valid, invalid and edge
cases.
'''

class CommonLettersException(Exception):
    pass


def three_most_common_letters(sentence):
    characters = list(sentence.lower())
    letters = []
    for character in characters:
        if 'a' <= character <= 'z':
            letters.append(character)
    letter_count = {}
    for letter in letters:
        if not letter in letter_count.keys():
            letter_count[letter] = 0
        letter_count[letter] = letter_count[letter] + 1
    return ['a', 'b', 'c']


if __name__ == '__main__':
    common_letters = three_most_common_letters('Write a function that takes in a sentence 3 most common letters.')
    for letter in common_letters:
        print(letter)