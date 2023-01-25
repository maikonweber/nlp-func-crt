from wordcloud import WordCloud
import matplotlib.pyplot as plt

# WordCloudPositive 

#Parms Text Dataframe - ColumaSentiment Reference[neg-pos] - 
def WordCloundPositive(text, columSentiment, ):
  classificacao = text[columSentiment].replace(["neg", "pos"], [0,1])
  text['class'] = classificacao


  texto_negativo = text.query("sentiment == 'pos'")
  todas_palavras = ' '.join([texto for texto in texto_negativo['text_pt']])
  nuvem_palavra = WordCloud(width=800, height=500, max_font_size=110).generate(todas_palavras)

  plt.figure(figsize=(10, 7))  
  plt.imshow(nuvem_palavra, interpolation='bilinear')
  plt.axis('off')
  plt.show()
  return


def WordCloundNegative(text, columSentiment):
  classificacao = text[columSentiment].replace(["neg", "pos"], [0,1])
  text['class'] = classificacao

  texto_negativo = text.query("sentiment == 'neg'")
  todas_palavras = ' '.join([texto for texto in texto_negativo['text_pt']])
  nuvem_palavra = WordCloud(width=800, height=500, max_font_size=110).generate(todas_palavras)


  plt.figure(figsize=(10, 7))  
  plt.imshow(nuvem_palavra, interpolation='bilinear')
  plt.axis('off')
  plt.show()
  return
