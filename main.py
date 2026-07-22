import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

###df = pd.read_csv("data/Online Retail.csv")
df = pd.read_csv("retail_data.csv", encoding="latin1")
df = df.drop(columns=['Country', 'Description'])

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

print(item_by_stockCode.describe()) 
### the most populat item is 85123A(white 
#hanging heart t-light holder) and was in 2035 orders,there are a total of 
#3663 items being accounted for it the data set

popular_item = df[item_by_stockCode =="85123A"]
print(popular_item["CustomerID"].value_counts())
print(popular_item.head(50))
###856 total groups order this product

###keep track of how many unique invoice numbers a person has, that means they are a returning customer

print(df["InvoiceNo"].value_counts()) ### biggest order made was 541, invoice number 576339, person 14096, in december
biggest_order_person = (df[df["CustomerID"] == 14096])
print(biggest_order_person)
print(biggest_order_person["InvoiceNo"].value_counts()) ### this person biggest orders happen around december christmas related items





'''
X_train, X_test, Y_train, Y_trust = train_test_split(


)
'''






