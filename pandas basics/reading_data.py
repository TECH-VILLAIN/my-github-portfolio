import pandas as pd
df = pd.read_csv("C:\\Users\\TECH_VILLAIN\\Downloads\\data.csv")
df.columns = df.columns.str.strip()
print(df.head())
x = df[['Duration']]
print(x)
print(df.loc[1,'Maxpulse'])
print(df.loc[0:2,'Pulse':'Calories'])
y = df[["Date"]]
print(y)
y = df[['Duration','Date']]
print(y)
new_index=[f"row{i}" for i in range(32)] 
df_new = df
df_new.index =new_index
print(df_new)
print(df_new.loc['row0':'row2','Duration':'Date'])