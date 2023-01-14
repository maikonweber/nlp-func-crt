import nltk

nltk.download('punkt')

def tokenize_word(split_text):
    split_word = nltk.tokenize.word_tokenize(split_text)
    print(split_word)
    return split_word

def split_only_words(split_word):
    lista_palavras = []
    for token in split_word:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

def normalize_tokens(split_only_words):
    lista_normalizada = []
    for palavra in split_only_words:
        print(palavra)
        lista_normalizada.append(palavra.lower())
    return lista_normalizada