import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage

# Read JSON File
json = pd.read_json("data.json")

# gabungin nilai x dan y
data = list(zip(json['x'], json['y']))

# Input dari Program
# x = [2, 3, 2, 2, 1, 3, 4, 6, 5, 4]
# y = [1, 2, 2, 3, 3, 1, 2, 3, 4, 4]
# data = list(zip(x, y))

# Methode Linkage
# 1. single
# 2. complete
# 3. average
# 4. weighted
# 5. centroid
# 6. median
# 7. ward
linkage_data = linkage(data, method='single', metric='euclidean')
dendrogram(linkage_data)

plt.show()
