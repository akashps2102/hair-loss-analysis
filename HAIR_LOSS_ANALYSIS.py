
import sys
print(sys.executable)

import sklearn
print(sklearn.__version__)

import pandas as pd 
df=pd.read_csv(r"C:\Users\abishek\OneDrive\Documents\hair loss.csv")
df.replace("No Data",pd.NA,inplace=True)
df.dropna(inplace=True)
pd.set_option('display.max_columns', None)
df.info
df.describe
df["Age Category"]=pd.cut(df["Age"],bins=[18,30,45,50],labels=["Young","Middle age","Old"])
print(df.groupby("Age Category")["Hair Loss"].sum())

print(df.groupby("Genetics")["Hair Loss"].sum())
print(df.groupby(["Age Category","Genetics"])["Hair Loss"].mean())

#Medical condition
print(df.groupby("Medical Conditions")["Hair Loss"].mean())

print(df.groupby("Medications & Treatments")["Hair Loss"].mean())

#Nutrition Deficiency
#print(df.groupby("Nutritional Deficiencies")["Hair Loss"].sum())


#Lifestyle related Mental stress inducing smoking and causing
print(df.groupby(["Stress","Smoking"])["Hair Loss"].mean())

df.columns = df.columns.str.strip()
print(df.groupby("Weight Loss")["Hair Loss"].mean())
print(df.groupby("Poor Hair Care Habits")["Hair Loss"].mean())

binary_cols = ["Genetics","Hormonal Changes","Smoking","Weight Loss",
               "Poor Hair Care Habits"]

for col in binary_cols:
    df[col] = df[col].map({"Yes":1,"No":0})
df["Stress"] = df["Stress"].map({"Low":1,"Moderate":2,"High":3})
df = pd.get_dummies(df, drop_first=True)
X = df.drop("Hair Loss", axis=1)
y = df["Hair Loss"]
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X, y)
importance = pd.Series(model.feature_importances_, index=X.columns)
importance = importance.sort_values(ascending=False)

print(importance.head(10))
