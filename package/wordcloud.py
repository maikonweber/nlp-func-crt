from wordcloud import WordCloud
import matplotlib.pyplot as plt

def wordcloud(allwords):
  nuvem_palavra = WordCloud(width=800, height=500, max_font_size=110).generate(allwords)  
  nuvem_palavra
  plt.figure()
  plt.imshow(nuvem_palavra)
  plt.show()
  return nuvem_palavra