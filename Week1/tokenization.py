import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o") #calling chatgpt model gpt-4o

print("Vocab size: ", encoder.n_vocab) # Print the vocabulary size == 200k

text = "Hello, how are you?"
tokens = encoder.encode(text)
print("Tokens: ", tokens) # Print the tokenized text

decode = encoder.decode(tokens)
print("Decoded: ", decode) # Print the decoded text