import pandas as pd
import numpy as np
import math as m
from sklearn.metrics.pairwise import cosine_similarity as cs
df=pd.read_csv("io.csv")
df=df[['name','usn','quality']]
quality=[]

for i in df['quality']:
 i=str(i)
 m=list(i.split(sep=","))
 for j in m:
  quality.append(j)
quality=list(set(quality))
print(quality)
