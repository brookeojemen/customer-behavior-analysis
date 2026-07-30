import pandas as pd
import matplotlib.pyplot as plot


df = pd.read_csv("data/retail_data.csv", encoding="latin1")
df = df.drop(columns=['Country', 'Description'])

fault_StockCode = ["POST", "DOT", "D"]

df = df.dropna()
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[~df["StockCode"].isin(fault_StockCode)]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


stock_codes = df["StockCode"]
invoice_numbers = df["InvoiceNo"]

df.info()
print(df.describe())
print(df.head(10))

print(stock_codes.describe()) 
print(stock_codes.value_counts())
### the most popular item is 85123A(white 
#hanging heart t-light holder) and was in 2035 orders,there are a total of 
#3663 items being accounted for it the data set

print(invoice_numbers.describe())
print(invoice_numbers.value_counts())
### biggest order made was 541, invoice number 576339, 
# 18480 unique invoice numbers 
# CustomerID 14096

popular_item = df[stock_codes =="85123A"]
print(popular_item["CustomerID"].value_counts())
print(popular_item.head(10))
###856 seperate purchases of this product

total_revenue_by_stockCode = df["Quantity"].mul(df["UnitPrice"]).groupby(df["StockCode"]).sum()
print(f"Item with highest revenue: {total_revenue_by_stockCode.idxmax()}")
print(total_revenue_by_stockCode.loc[total_revenue_by_stockCode.idxmax()])
print(total_revenue_by_stockCode.sort_values(ascending=False).head(5))
### StockCode: 23843, brings in 168469.6

biggest_order_person = (df[df["CustomerID"] == 14096])
print(biggest_order_person)
print(biggest_order_person["InvoiceNo"].value_counts()) 
print(biggest_order_person["StockCode"].value_counts()) 
### this person biggest orders happen around december christmas related items
# makes many big orders
# buys stock item 23263 item the most


orders_per_customer = invoice_numbers.groupby(df["CustomerID"]).nunique()
print(orders_per_customer.describe())
print(f"Top returning Customer:{orders_per_customer.idxmax()}")
print(orders_per_customer[orders_per_customer>= 50])
print(orders_per_customer[orders_per_customer != 1])
print(orders_per_customer.loc[14096])
top_returning_customers = orders_per_customer.sort_values(ascending=False).head(5)
print(top_returning_customers)
### most returned customer returned 209 times
# 4338 total unique customers 
# CustomerID 14096 has 17 invoices, but makes big orders
# 2837/4338 of customers are returning
# 1501/4338 of customers are not returning


total_quantity_per_customer= df["Quantity"].groupby(df["CustomerID"]).sum()
total_spent_per_customer = df["Quantity"].mul(df["UnitPrice"]).groupby(df["CustomerID"]).sum()
average_order_value = total_spent_per_customer/orders_per_customer
recent_date = df["InvoiceDate"].max()
print(f"Most recent date : {recent_date}")
recent_customer_order = df["InvoiceDate"].groupby(df["CustomerID"]).max()
recency_delta = recent_date - recent_customer_order
recency = recency_delta.dt.days
### RFM

customer_metrics_df = pd.DataFrame({
    "Orders": orders_per_customer, 
    "Total Quantity": total_quantity_per_customer, 
    "Total Spent": total_spent_per_customer, 
    "Average Order Value": average_order_value,
    "Recency": recency
})

print(customer_metrics_df.head())
print(customer_metrics_df.describe())

order_counts = customer_metrics_df["Orders"].value_counts().sort_index()


plot.figure()
plot.bar(order_counts.index, order_counts.values)
plot.xlabel("Number of Orders")
plot.ylabel("Number of Customers")
plot.title("Customer Order Frequency")
plot.savefig("images/Customer Order Frequency.png")

plot.figure()
plot.hist(customer_metrics_df["Total Spent"], bins=30)
plot.xlabel("Total Amount Spent")
plot.ylabel("Number of Customers")
plot.title("Total Customer Spending")
plot.savefig("images/Total Customer Spending.png")

plot.figure()
plot.scatter(customer_metrics_df["Orders"],customer_metrics_df["Total Spent"], alpha=0.3, s = 10 )
plot.xlabel("Number of Orders")
plot.ylabel("Total Amount Spent")
plot.title("Orders vs Total Spent")
plot.savefig("images/Orders vs Total Spent.png")

print(customer_metrics_df[["Orders", "Total Spent"]].corr())
print(customer_metrics_df[["Orders", "Total Quantity"]].corr())

