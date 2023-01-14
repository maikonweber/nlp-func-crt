from package.tokenize import tokenize_word,split_only_words, normalize_tokens
from package.freq_ import freq_disk, prob

with open("artigos.txt", "r") as f:
    artigos = f.read()

len(artigos)

tokenize_ = tokenize_word(artigos)
print(tokenize_)
slip = split_only_words(tokenize_)
print(slip)
nr = normalize_tokens(slip)

lp = freq_disk(nr)
print(lp)

total = len(nr)
print(total)
lp = prob('e', total, nr)


