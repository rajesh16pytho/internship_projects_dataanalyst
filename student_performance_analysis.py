import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('students.csv')
df['Total']=df[['Math','Science','English']].sum(axis=1)
df['Average']=df['Total']/3
df['Result']=df['Average'].apply(lambda x:'Pass' if x>=50 else 'Fail')
print(df)
print(df[['Math','Science','English']].mean())
df[['Math','Science','English']].mean().plot(kind='bar')
plt.show()
df.to_csv('Student_Report.csv',index=False)
