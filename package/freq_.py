import nltk

def freq_disk(list):
    frequencia = nltk.FreqDist(list)
    frequencia.most_common(10)
    return frequencia.most_common(10)


def prob(word_gen, total_word, list):
    return freq_disk(list)[word_gen]/total_word