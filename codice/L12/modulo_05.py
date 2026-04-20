# Installare pandas: pip install pandas
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('moto.csv')

#print(df.head())
# print(df.shape)
# print(df.columns)   
# print(df.dtypes)
# print(df.info())
# print(df[["Modello","Prezzo (€)"]])

# for i in range(0, len(df)):
#     print(df.iloc[i, 1:3])
#     print("\n\n\n")

# df_max_20000 = df[df["Prezzo (€)"] > 20000]

# df_max_20000.plot()

# matplotlib.pyplot.show()


df.to_html("moto.html")
df.to_excel("moro.xlsx")
