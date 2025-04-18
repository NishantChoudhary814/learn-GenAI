class Vocabulary:
    def __init__(self):
        # Stores word → unique index mapping
        self.dictionary = dict()
        
        # Tracks the size of the vocabulary (number of unique words)
        self.vocab_size = 0
        
        # Stores index → word mapping (reverse lookup)
        self.reverse_dictionary = dict()

    def add_word(self, word):
        """
        Add a word to the vocabulary if it doesn't already exist.
        Assigns a new unique ID to the word.
        """
        if word not in self.dictionary:
            # Assign next available ID (starting from 1)
            self.dictionary[word] = self.vocab_size + 1
            self.reverse_dictionary[self.vocab_size + 1] = word
            self.vocab_size += 1

    def get_word(self, index):
        """
        Given an index (ID), return the corresponding word.
        Returns None if the index is not present.
        """
        if index in self.reverse_dictionary:
            return self.reverse_dictionary[index]
        else:
            return None
        
    def get_index(self, word):
        """
        Given a word, return its index (ID).
        Returns None if the word is not in the vocabulary.
        """
        if word in self.dictionary:
            return self.dictionary[word]
        else:
            return None
        
    def is_word_present(self, word):
        """
        Check if a word exists in the vocabulary.
        Returns True or False.
        """
        return word in self.dictionary
    
    def is_token_present(self, token):
        """
        Check if a token ID exists in the reverse dictionary.
        Useful to verify if a decoded index is valid.
        """
        return token in self.reverse_dictionary
        
    def get_vocab_size(self):
        """
        Returns the total number of words in the vocabulary.
        """
        return self.vocab_size
    
    def get_dictionary(self):
        """
        Returns the full word → index dictionary.
        Useful for saving or exporting the vocabulary.
        """
        return self.dictionary
