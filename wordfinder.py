class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        self.file = open(file, "r")
        self.words = self.extract_words()

    def __repr__(self):
        return f"<{len(self.words)} words read>"

    def extract_words(self):
        text = self.file.read()
        words = text.split()
        return words

    def random(self):
        from random import choice
        return choice(self.words)