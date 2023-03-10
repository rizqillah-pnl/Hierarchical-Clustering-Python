import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage

# Read JSON File
# dataJson = pd.read_json("data.json")
# Convert to CSV
# dataJson.to_csv("data.csv")

dataJson = pd.read_csv("data.csv")

# gabungin nilai x dan y
data = list(zip(dataJson['x'], dataJson['y']))

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
plt.title("Grafik Dendogram", fontweight="bold")
plt.show()
