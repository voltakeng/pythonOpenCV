import pandas as pd

df = pd.read_csv("data.csv")

print(df)

bill = ["itching","skin_rash","nodal_skin_eruptions","dischromic _patches"]

for i in range(len(bill)):
  df.iat[0,i+1] = bill[i]

print(df)
