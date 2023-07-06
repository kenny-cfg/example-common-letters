from collections import Counter


class CommonLettersException(Exception):
    pass


def three_most_common_letters(sentence):
    characters = list(sentence.lower())
    letters = []
    for character in characters:
        if 'a' <= character <= 'z':
            letters.append(character)
    letter_count = Counter(letters)
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
    if most_common_letter is None or next_most_common_letter is None or third_most_common_letter is None:
        raise CommonLettersException
    return [most_common_letter, next_most_common_letter, third_most_common_letter]


if __name__ == '__main__':
    common_letters = three_most_common_letters('Hello world')
    for letter in common_letters:
        print(letter)
