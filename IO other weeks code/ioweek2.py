import pandas as pd
import numpy as np
df=pd.read_csv("io.csv")
print("Top 5 entries are:-",df.head())
print("25th row 3rd column element is",df.iat[24,2])
print(df["email id"][24])
print("Names of the students in descending order is",df.sort_values("name",ascending=False))
