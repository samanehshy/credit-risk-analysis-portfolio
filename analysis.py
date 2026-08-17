from pandas._libs import properties
import pandas as pd
import sqlite3
df = pd.read_csv('credit_risk_dataset.csv')
print(df.head())
print(df.info())
mean_val = df['loan_int_rate'].mean() 
print(mean_val)
df['loan_int_rate'] = df['loan_int_rate'].fillna(mean_val)
print(df.isnull().sum())
mean_val=df['person_emp_length'].mean()
print(mean_val)
df['person_emp_length']=df['person_emp_length'].fillna(mean_val)
print(df.isnull().sum())

df.to_csv('cleaned_credit_risk.csv', index=False)

print("cleaned_credit_risk.csv is created successfully")