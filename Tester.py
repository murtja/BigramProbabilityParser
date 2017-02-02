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

if __name__ == '__main__':
    unittest.main()
