import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('chemistry_data.csv')
df['Category']=df['Concentration_M'].apply(lambda x:'Concentrated' if x>=1 else 'Dilute')
print(df)
print(df['Concentration_M'].mean())
print(df['Density_g_ml'].mean())
print(df['Category'].value_counts())
plt.bar(df['Compound'],df['Concentration_M'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
df.to_csv('Chemistry_Report.csv',index=False)
