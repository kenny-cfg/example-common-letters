import unittest

from index import CommonLettersException, three_most_common_letters


class TestIndex(unittest.TestCase):
    def test_not_enough_distinct_letters(self):
        source = 'aaaabbbbb'

        with self.assertRaises(CommonLettersException) as context:
            three_most_common_letters(source)

    def test_happy_path(self):
        source = 'abcabc aa b d'
        expected = ['a', 'b', 'c']

        actual = three_most_common_letters(source)

        self.assertEquals(expected, actual)
