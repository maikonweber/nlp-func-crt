
from package.freq_ import freq_disk, prob
from package.sqlpointer import select_data
from package.fn_bigrma import fun_bigrama, containtiment
from package.tokenize import split_only_words, normalize_tokens, tokenize_word, model_pt, bi_gram
import pandas as pd
import nltk


# allwordtext = []
# all = []
rows = select_data(1)
place = rows[0][0]
about = rows[0][2]

href = rows[0][3]

text = tokenize_word(about)
text_ = split_only_words(text)
text_2 = normalize_tokens(text_)
Togged = model_pt(about)
bi = fun_bigrama(about, about, 2)
print(print)

# rows = select_data(1)
# place = rows[0][0]
# about = rows[0][2]
# href = rows[0][3]

#         #  tokenize_text1 = tokenize_word(href)
#          nextext = []

#          for i in href:
#             dict = {
#               i['href'] : tokenize_word(i['text'])
#             }
#             nextext.append(dict)

#          allwordtextabout = []


#          dict = {
#              "place" : place,
#              "about" : about,
#              "token" : tokenize_,
#              "text1" : href,
#              "tokenize" : nextext
#           }

#          all.append(dict)

# #         all.append(dict)
# #         for i in tokenize_:
# #             allwordtext.append(i)

# df = pd.DataFrame.from_records(all)

# df.to_csv('place.csv')
# # for i in df:
# #     print(i)
# # # nr = normalize_tokens(allwordtext)
# # # sp = split_only_words(nr)
# # # freq = freq_disk(sp)

# # # from package.wordcloud import wordcloud

# # # wordcloud(allwordtext)
