import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def pareto_char(data):
  plt.figure(figsize=(12,8))
  ax = sns.barplot(data = data, x = "Palavra", y = "Frequência", color = 'gray')
  ax.set(ylabel = "Contagem")
  return plt.show()
