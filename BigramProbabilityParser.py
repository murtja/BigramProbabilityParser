class BigramProbabilityParser():

    def __init__(self):
        self.db = {}
        self.ignore_list = []

    def load(self, filename):

        with open(filename, 'r') as file_handle:
            all_lines = ""

            for line in file_handle:
                all_lines += all_lines + " " + line

            clean_line = self.clean(line)
            bigrams = self.extract(clean_line)
            self.add(bigrams)

    def get_unique_words_count(self):
        return len(self.db)

    def get_bigram_count(self):
        total = 0

        for first_word in self.db:
            for second_word in self.db[first_word]:
                bigram_pair_count = self.db[first_word][second_word]

                total += bigram_pair_count

        return total

    def clean(self, string):
        result = ""

        for letter in string:
            if letter.isalpha() or letter.isspace():
                result += letter.lower()

        return result

    def extract(self, clean_string):
        result = []

        last_word = None

        for word in clean_string.split():
            if word in self.ignore_list:
                continue

            if last_word is None:
                last_word = word
                continue

            result.append((last_word, word))
            last_word = word

        return result

    def add(self, bigrams):

        for bigram in bigrams:

            current_words = self.db.get(bigram[0], {})
            current_count = current_words.get(bigram[1], 0)

            current_words[bigram[1]] = current_count + 1
            self.db[bigram[0]] = current_words

        return None



