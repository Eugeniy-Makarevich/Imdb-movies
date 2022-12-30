#  add Index to dataset to prevent duplications
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = ' '.join(row+' ' for row in dataset['genre'])
x, y = np.ogrid[:800, :800]

wc = WordCloud(mode='RGBA', background_color = None, repeat = True, 
               collocations = False,colormap='Wistia',)
wc.generate(text)
plt.rcParams['savefig.facecolor'] = '#343333'
plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()
