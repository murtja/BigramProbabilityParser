import unittest
from BigramProbabilityParser import BigramProbabilityParser


class TestStringMethods(unittest.TestCase):

    ######################################################################
    # Increment 1
    ######################################################################

    def test_clean_up(self):
        b = BigramProbabilityParser()

        str = "Hello, my name is joe. Bye! Bye!"

        expected = "hello my name is joe bye bye"
        result = b.clean(str)

        self.assertEqual(expected, result)

    def test_bigram_extract(self):
        b = BigramProbabilityParser()

        str = "hello my name"

        expected = [('hello', 'my'), ('my', 'name')]
        result = b.extract(str)

        self.assertEqual(expected, result)

    def test_add_to_db(self):
        b = BigramProbabilityParser()

        str = "Hello, my name is joe. Bye! Bye!"

        cleaned_str = b.clean(str)
        bigrams = b.extract(cleaned_str)

        b.add(bigrams)

        expected = 6
        actual = b.get_unique_words_count()

        self.assertEqual(expected, actual)

    def test_full(self):
        b = BigramProbabilityParser()
        b.load("file1.txt")

        expected = 12
        actual = b.get_bigram_count()

        self.assertEqual(expected, actual)

    ######################################################################
    # Increment 2
    ######################################################################

    def test_ignore_words(self):
        b = BigramProbabilityParser()
        b.ignore_list = ['my', 'is']

        str = "Hello, my name is joe. Bye! Bye!"

        cleaned_str = b.clean(str)
        bigrams = b.extract(cleaned_str)

        b.add(bigrams)

        expected = 4
        actual = b.get_unique_words_count()

        self.assertEqual(expected, actual)

    def test_full_with_ignore(self):
        b = BigramProbabilityParser()
        b.ignore_list = ['my', 'is']

        b.load("file1.txt")

        expected = 9
        actual = b.get_bigram_count()

        self.assertEqual(expected, actual)

    def test_probable(self):
        b = BigramProbabilityParser()

        b.load("file1.txt")

        expected = "name"
        actual = b.get_probable_word("my")

        self.assertEqual(expected, actual)

    def test_probable_with_ignore(self):
        b = BigramProbabilityParser()
        b.load("file2.txt")

        expected = "for"
        actual = b.get_probable_word("looking")

        self.assertEqual(actual, expected)

        b = BigramProbabilityParser()
        b.ignore_list = ['for', 'a', 'like']
        b.load("file2.txt")

        expected = "carrot"
        actual = b.get_probable_word("looking")

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
