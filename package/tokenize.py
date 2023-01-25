
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk.util import ngrams  
import spacy

def bi_gram(token, n):
    bigrams =  ngrams(token, n)
    return list(bigrams)

def model_pt_verbs(text): 
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(text)
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    
    return verbs
# Only to Rus in English
# def token_to_tag(split_word):
#     tagged_tokens = pos_tag(split_word, lang='por')
    
#     print(tagged_tokens)
#     return tagged_tokens

def tokenize_word(split_text):
    split_word = nltk.tokenize.word_tokenize(split_text, language='portuguese')
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
        lista_normalizada.append(palavra.lower())
    return lista_normalizada
7

