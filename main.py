import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plot

###df = pd.read_csv("data/Online Retail.csv")
df = pd.read_csv("retail_data.csv", encoding="latin1")
df = df.drop(columns=['InvoiceNo', 'Country', 'Description'])

fault_StockCode = ["POST", "DOT", "D"]

df = df.dropna()
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[~df["StockCode"].isin(fault_StockCode)]

quantity = df["Quantity"]
item_by_stockCode = df["StockCode"]

df.info()
print(df.describe())
print(df.head(10))

### make a bar graph to see the most bought items, then ill make another graph too see of those customers 
### bought it if they are buying it more than once
### thought process, add up quantityes for each stockcode using a forloop maybe

print(item_by_stockCode.describe())


