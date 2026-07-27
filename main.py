import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans

df = pd.read_csv("data/retail_data.csv", encoding="latin1")
df = df.drop(columns=['Country', 'Description'])

fault_StockCode = ["POST", "DOT", "D"]

df = df.dropna()
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[~df["StockCode"].isin(fault_StockCode)]


StockCode = df["StockCode"]
InvoiceNo = df["InvoiceNo"]

df.info()
print(df.describe())
print(df.head(10))

print(StockCode.describe()) 
print(df["StockCode"].value_counts())
### the most popular item is 85123A(white 
#hanging heart t-light holder) and was in 2035 orders,there are a total of 
#3663 items being accounted for it the data set

print(InvoiceNo.describe())
print(df["InvoiceNo"].value_counts())
### biggest order made was 541, invoice number 576339, 
# 18480 unique invoice numbers 
# CustomerID 14096

popular_item = df[StockCode =="85123A"]
print(popular_item["CustomerID"].value_counts())
print(popular_item.head(10))
###856 seperate purchases of this product


biggest_order_person = (df[df["CustomerID"] == 14096])
print(biggest_order_person)
print(biggest_order_person["InvoiceNo"].value_counts()) 
print(biggest_order_person["StockCode"].value_counts()) 
### this person biggest orders happen around december christmas related items
# makes many big orders
# buys stock item 23263 item the most


unique_InvoiceNo = df["InvoiceNo"].groupby(df["CustomerID"]).nunique()
print(unique_InvoiceNo.describe())
print(unique_InvoiceNo.info)
print(unique_InvoiceNo.idxmax())
print(unique_InvoiceNo[unique_InvoiceNo >= 50])
print(unique_InvoiceNo[unique_InvoiceNo != 1])
print(unique_InvoiceNo.loc[14096])
### most returned customer returned 209 times
# 4338 total unique customers 
# CustomerID 14096 has 17 invoices, but makes big orders
# 2837/4338 of customers are returning
# 1501/4338 of customers are not returning

ID12748 = df[df["CustomerID"] == 12748]
ID14911 = df[df["CustomerID"] == 14911]
ID17841 = df[df["CustomerID"] == 17841]

print(ID12748.head(10))
print(ID14911.head(10))
print(ID17841.head(10))

print(ID12748["InvoiceNo"].value_counts()) 
print(ID14911["InvoiceNo"].value_counts()) 
print(ID17841["InvoiceNo"].value_counts()) 
### Top 3 returners, all over 100
# multiple smaller orders in comparison to CustomerID 14096









'''
X_train, X_test, Y_train, Y_trust = train_test_split(


)
'''






