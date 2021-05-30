import pandas as pd
import numpy as np
import math as m
from sklearn.metrics.pairwise import cosine_similarity as cs
df=pd.read_csv("io.csv")
df=df[['name','usn','quality']]
quality=[]
q=[]

for i in df['quality']:
 i=str(i)
 m=list(i.split(sep=","))
 q.append(list(m))
 for j in m:
  quality.append(j)
quality=list(set(quality))
print(quality)
#quality=["",""]

page_profile_matrix=[]
for i in range(len(df['quality'])):
    page_profile_matrix.append(list())


for i in range(len(q)):
    for j in range(len(quality)):
        if quality[j] in q[i]:
            page_profile_matrix[i].append(1)
        else:
            page_profile_matrix[i].append(0)

cosine_sim=cs(page_profile_matrix)

print(cosine_sim)

scores_series=pd.Series(cosine_sim[3]).sort_values(ascending=False)
recommended_pages_indexes=list(scores_series[0:5].index)
recommended_pages=[]
for i in recommended_pages_indexes:
    recommended_pages.append(df["name"][i])
print(recommended_pages)
