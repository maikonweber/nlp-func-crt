from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

def class_text(texto, coluna, coluna_class):
  vetorizar = CountVectorizer(lowercase=False, max_features=50)
  bag_of_words = vetorizar.fit_transform(texto[coluna])

  # print(bag_of_words)
  # matriz_esparsa = pd.DataFrame.sparse.from_spmatrix(bag_of_words, columns=vetorizar.get_feature_names_out())
  # print(matriz_esparsa)
  # print(resenha)
  
  treino, teste, classe_treino, classe_teste = train_test_split(bag_of_words,
                                                              texto[coluna_class],
                                                              random_state = 42)

  regressao_logistica = LogisticRegression(solver = 'lbfgs')
  regressao_logistica.fit(treino, classe_treino)
  acuracia = regressao_logistica.score(teste, classe_teste)
  print(acuracia)
  return acuracia