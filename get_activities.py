import pandas as pd
import numpy as np
from datetime import datetime

import sys

df_activities=pd.read_csv("./data/activities.csv",index_col=[0])

print(df_activities.loc[df_activities["rank"]==1].loc[:,"activities"])

print("What activities did you do ?")
#a=input()
a=sys.argv[1]

df_h = pd.read_csv("data/history.csv", index_col=[0])



if a.lower() in df_activities.loc[:,'activities'].str.lower().tolist():
    print("OK, let's turn the wheel of fortune.")
    #run the script rirt if the activity is a useful one
    import rirt

    df_h = pd.concat([df_h,
           pd.DataFrame([[datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            a,
            df_activities.loc[df_activities.activities.str.lower()==a.lower()].loc[:,"subcategory"].tolist()[0],
            df_activities.loc[df_activities.activities.str.lower()==a.lower()].loc[:,"category"].tolist()[0],
            np.nan,
            np.nan]],columns=["date","activity","subcategory","category","rewards","price"])
          ])
else:
    print("Oh, focus on the useful tasks.")

df_h.to_csv("data/history.csv")
