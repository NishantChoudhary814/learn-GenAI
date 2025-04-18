import re
from dictionary import Vocabulary

vocab = Vocabulary()
class Tokenizer:
    
    def __init__(self, text):
        self.text = text
        self.tokens = []
        
    def separate(self):
        # Split the text into words and punctuation of Hindi and Englisg
        # Devanagari : \u0900-\u097F
        # Latin (English) : A-Za-z

        pattern = r'[\u0900-\u097F]+|[A-Za-z]+|\d+|[.,!?।]|[\s]+'
        words = re.findall(pattern,self.text);

        wordsArray = [word for word in words if not word.isspace()] # Remove empty strings from the list
        return wordsArray
    
    def encode(self,text=None):
        if text is None:
            text = self.text
            tokens = self.separate() # Tokenize the text
        else:
            tokens = self.separate(text)

        # Create a vocabulary object
        # Add each token to the vocabulary
        for token in tokens:
            if not vocab.is_word_present(token):
                vocab.add_word(token)

        # Encode the tokens
        encoded_tokens = [vocab.get_index(token) for token in tokens]
        return encoded_tokens

    def decode(self, encoded_tokens):
        # Create a vocabulary object
        # Decode the tokens using the reverse dictionary
        decoded_tokens = [vocab.get_word(token) for token in encoded_tokens]
        return decoded_tokens
   


obj = Tokenizer("Hello, this is a test. यह एक परीक्षण है। ")
vocab=Vocabulary()
print(obj.separate())
# Output: ['Hello', ',', 'this', 'is', 'a', 'test', '.', 'यह', 'एक', 'परीक्षण', 'है', '।']
print(obj.encode())
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(obj.decode([1, 10, 11]))
# Output: ['Hello', ',', 'this', 'is', 'a', 'test', '.', 'यह', 'एक', 'परीक्षण', 'है']
