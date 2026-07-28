import pandas as pd
import matplotlib.pyplot as plot
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("data/retail_data.csv", encoding="latin1")
df = df.drop(columns=['Country', 'Description','InvoiceDate'])

fault_StockCode = ["POST", "DOT", "D"]

df = df.dropna()
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[~df["StockCode"].isin(fault_StockCode)]


orders_per_customer = df["InvoiceNo"].groupby(df["CustomerID"]).nunique()
total_quantity_per_customer= df["Quantity"].groupby(df["CustomerID"]).sum()
total_spent_per_customer = df["Quantity"].mul(df["UnitPrice"]).groupby(df["CustomerID"]).sum()
average_order_value = total_spent_per_customer/orders_per_customer


customer_metrics_df = pd.DataFrame({
    "Orders": orders_per_customer, 
    "Total Quantity": total_quantity_per_customer, 
    "Total Spent": total_spent_per_customer, 
    "Average Order Value": average_order_value
})
