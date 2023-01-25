from package.tokenize import tokenize_word, split_only_words, normalize_tokens
from package.freq_ import freq_disk, prob
from package.sqlpointer import select_data, cursor
from package.tokenize import split_only_words, normalize_tokens
import pandas as pd
import nltk

data = select_data(1)
place = data[0][1]
about = data[0][2]
print(about)
tokenize = ''
cur = cursor()
tokenize = tokenize_word(about)
split = split_only_words(tokenize)

print(tokenize)
try:
    cur.execute('BEGIN')
    cur.execute('Alter Table travel_book Add Column tokenize_about')
    cur.execute('COMMIT')
except:
    cur.execute('Rollback')
finally:
    cur.execute('COMMIT')
try:
    cur.execute('BEGIN')
    cur.execute(f'Update travel_book SET tokenize_about = {tokenize} WHERE id = 1')
except:
    cur.execute('Rollback')
finally:
    cur.execute('COMMIT')
