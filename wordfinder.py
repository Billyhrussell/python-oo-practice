class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """Generates list of words from a dictionary"""
        file = open(file, "r")
        self.words = self.extract_words(file)

    def __repr__(self):
        """Displays number of words read"""
        return f"<{len(self.words)} words read>"

    def extract_words(self, file):
        """Extracts the words from the dictionary and puts them into a list"""
        # text = file.read()
        return [line.strip() for line in file]

    def random(self):
        """Randomly selects a word from the list"""
        from random import choice
        return choice(self.words)

class SpecialWordFinder(WordFinder):

    def extract_words(self, file):
        """Extracts the words from the dictionary and puts them into a list
        and filters out comments and empty lines"""

        words = super().extract_words(file)
        return [word for word in words if not word.startswith('#') and not word == '']
