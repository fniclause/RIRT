import numpy as np
from numpy import random
import pandas as pd

df_recompenses = pd.read_csv("./data/recompenses.csv",index_col=0)

l_recompenses = df_recompenses.index.values.tolist()


a = random.normal(0,1)

test = []
if a <-1 :
    print("test random")
elif -1<a<=0:
    print("pas de recompense")
else:
    b = random.choice(l_recompenses)
    print(f"Bravo, tu te rapproches de l'objectif : {b} => +{round(a,2)}€")
    df_recompenses.loc[b,"déjà acquis"]=round(a,2)
    
df_recompenses.to_csv("./data/recompenses.csv")