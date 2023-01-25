import numpy as np  
from sklearn.feature_extraction.text import CountVectorizer

def fun_bigrama(fonte, comparar, n): 
    counts = CountVectorizer(analyzer='word', ngram_range=(n, n))
    vocabb2int = counts.fit([comparar, fonte]).vocabulary_
    
    print(vocabb2int)
    return vocabb2int

def containtiment (ngram):
    # Fazer a interseçao e comparação   
    intersection = np.amin(ngram.toarray(), axis = 0)
    intersection_count = np.sum(intersection)

    index_a = 0
    A_count = np.sum(ngram.toarray()[index_a])
    A_count

    intersection_count / A_count

    