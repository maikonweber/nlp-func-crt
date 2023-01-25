import pandas as pd


def dataframe_classification_allWords(archive, col):
  resenha = pd.read_csv(archive)
  print(resenha[col].head())
# Classifica a Resenha em 0, 1 para negativos e positivo
  classificacao = resenha[col].replace(["neg", "pos"], [0,1]) 
  resenha['class'] = classificacao
  todas_palavras = ' '.join([texto for texto in resenha['text_pt']])
  print('This is you dataframe')
  return todas_palavras