import os
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

f = open('PDAreaCabData.csv', "r")

linecount = 0

lats = []
longs = []

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount%2==0:
        linecount +=1
        continue
    else:
        lat= row[1]
        long= row[2]
        lats.append(lat)
        longs.append(long)
        linecount+=1

x1 = np.array(lats)
x2 = np.array(longs)



# create new plot and data
plt.plot()
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

# k means determine k
distortions = []
K = range(200,4000,200)
for k in K:
    print(k)
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    print(distortions)
    
# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

        
