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
    for individual_letter in letters:
        if individual_letter not in letter_count.keys():
            letter_count[individual_letter] = 0
        letter_count[individual_letter] = letter_count[individual_letter] + 1
    most_common_letter = None
    next_most_common_letter = None
    third_most_common_letter = None
    for individual_letter in letter_count:
        count = letter_count[individual_letter]
        if most_common_letter is None or count > letter_count[most_common_letter]:
            third_most_common_letter = next_most_common_letter
            next_most_common_letter = most_common_letter
            most_common_letter = individual_letter
        elif next_most_common_letter is None or count > letter_count[next_most_common_letter]:
            third_most_common_letter = next_most_common_letter
            next_most_common_letter = individual_letter
        elif third_most_common_letter is None or count > letter_count[third_most_common_letter]:
            third_most_common_letter = individual_letter
    return [most_common_letter, next_most_common_letter, third_most_common_letter]


if __name__ == '__main__':
    common_letters = three_most_common_letters('Write a function that takes in a sentence 3 most common letters.')
    for letter in common_letters:
        print(letter)
