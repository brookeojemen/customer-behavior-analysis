import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plot

###df = pd.read_csv("data/Online Retail.csv")
df = pd.read_csv("retail_data.csv", encoding="latin1")
df = df.drop(columns=['InvoiceNo', 'Description', 'Country'])

fault_StockCode = ["POST", "DOT", "D"]

df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[~df["StockCode"].isin(fault_StockCode)]

df.value_counts("StockCode")
df.value_counts("CustomerID")

df.info()
print(df.describe())
print(df.head(60))

