import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [2, 3, 2, 2, 1, 3, 4, 6, 5, 4]
y = [1, 2, 2, 3, 3, 1, 2, 3, 4, 4]

data = list(zip(x, y))

linkage_data = linkage(data, method='complete', metric='euclidean')
dendrogram(linkage_data)

plt.show()
