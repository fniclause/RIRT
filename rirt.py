import numpy as np
from numpy import random

a = random.normal(0,1)

recompenses = ["Cadre velo","Bouquet de fleurs","Livre victoire","Dérailleur arriere","Pantalon","Chemise blanche","Tri fonction"]
test = []
if a <-1 :
    print("test random")
elif -1<a<=0:
    print("pas de recompense")
else:
    print("recompense random")
    b = random.choice(recompenses)
    print(f"{b} : +{round(a,2)}€")