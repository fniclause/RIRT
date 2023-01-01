import numpy as np
from numpy import random
import pandas as pd

df_rewards = pd.read_csv("./data/rewards.csv",index_col=0)

l_rewards = df_rewards.index.values.tolist()


a = random.normal(0,1)

test = []
if a <-1 :
    print("test random")
elif -1<a<=0:
    print("Pas de recompense")
else:
    b = random.choice(l_rewards)
    print(f"Bravo, tu te rapproches de l'objectif : {b} => +{round(a,2)}€")
    df_rewards.loc[b,"already"]=round(a,2)
    
df_rewards["pourcentage"]=round(df_rewards["already"]/df_rewards["price"]*100)
    
df_rewards.to_csv("./data/rewards.csv")
print(df_rewards)