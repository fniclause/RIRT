import pandas as pd

df_activities=pd.read_csv("./data/activities.csv",index_col=[0])

print(df_activities.loc[df_activities["rank"]==1].loc[:,"activities"])

print("What activities did you do ?")
a=input()


if a.lower() in df_activities.loc[:,'activities'].str.lower().tolist():
    print("OK, let's turn the wheel of fortune.")
    #run the script rirt if the activity is a useful one
    import rirt
else:
    print("Oh, focus on the useful tasks.")

