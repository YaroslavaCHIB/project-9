import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('C:\\Users\\teacher\\Desktop\\дз\\final_DataFrame.csv')
print(df)

labelencoder=LabelEncoder()
df['activity']=labelencoder.fit_transform(df['activity'])
print(df)

labelencoder=LabelEncoder()
df['name']=labelencoder.fit_transform(df['name'])
print(df)

model = KMeans(n_clusters = 5)
X = df.iloc[:,[2]].values
y = df.iloc[:,[3]].values
print(X)
print(y)
 
model.fit(X)

import matplotlib.pyplot as plt

score = []

for i in range(3,15):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    tmp = kmeans.inertia_
    score.append(tmp)

plt.plot(range(3,15), score)
