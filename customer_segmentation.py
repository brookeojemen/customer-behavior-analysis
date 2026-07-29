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

customer_metrics_df.info()
print(customer_metrics_df.describe())
features = customer_metrics_df[["Orders", "Total Quantity", "Total Spent"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
###Scaling the features to ensure equal contribution to clustering

elbow_k_values = []
silhouette_values = []
cluster_k = 10
for i in range (1,cluster_k+1):
    kmeans = KMeans(n_clusters= i, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    elbow_k_values.append(kmeans.inertia_)

plot.plot(range(1,cluster_k + 1), elbow_k_values, marker = "o")
plot.xlabel("Number of Clusters")
plot.ylabel("Inertia")
plot.title("Elbow Plot")
###Elbow Method to determine which value of K would be the best fit
## k = 4 potentially best option

for i in range(2, cluster_k+1):
    kmeans = KMeans(n_clusters= i, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    fit_labels = kmeans.labels_
    score = silhouette_score(scaled_features, fit_labels)
    silhouette_values.append(score)
print(silhouette_values)

plot.figure()
plot.plot(range(2, cluster_k + 1), silhouette_values, marker="o")
plot.xlabel("Number of Clusters")
plot.ylabel("Silhouette Score")
plot.title("Silhouette Score by Number of Clusters")
###Silhouette Score
## k = 2 potentially best option

kmeans_2 = KMeans(n_clusters= 2, random_state=42, n_init=10)
customer_metrics_df["Cluster_2"] = kmeans_2.fit_predict(scaled_features)
centroids_2 = scaler.inverse_transform(kmeans_2.cluster_centers_)
plot.figure()
plot.scatter(customer_metrics_df["Orders"],customer_metrics_df["Total Quantity"], c=kmeans_2.labels_,  alpha=0.3, s = 10)
plot.scatter(
    centroids_2[:, 0], 
    centroids_2[:, 1],
    marker ="X",
    s = 20,
    label = "Centroids"
)
plot.xlabel("Number of Orders")
plot.ylabel("Total Amount of Items")
plot.title("Orders vs Items")
plot.legend()

plot.figure()
plot.scatter(customer_metrics_df["Orders"],customer_metrics_df["Total Spent"], c=kmeans_2.labels_, alpha=0.3, s = 10)
plot.scatter(
    centroids_2[:, 0], 
    centroids_2[:, 2],
    marker ="X",
    s = 20,
    label = "Centroids"
)
plot.xlabel("Number of Orders")
plot.ylabel("Total Amount Spent")
plot.title("Orders vs Total Spent")
plot.legend()
print(kmeans_2.labels_)
print(centroids_2)
### plots for k = 2


kmeans_4 = KMeans(n_clusters= 4, random_state=42, n_init=10)
customer_metrics_df["Cluster_4"] = kmeans_4.fit_predict(scaled_features)
centroids_4 = scaler.inverse_transform(kmeans_4.cluster_centers_)
plot.figure()
plot.scatter(customer_metrics_df["Orders"],customer_metrics_df["Total Quantity"], c=kmeans_4.labels_,  alpha=0.3, s = 10)
plot.scatter(
    centroids_4[:, 0], 
    centroids_4[:, 1],
    marker ="X",
    s = 20,
    label = "Centroids"
)
plot.xlabel("Number of Orders")
plot.ylabel("Total Amount of Items")
plot.title("Orders vs Items")
plot.legend()

plot.figure()
plot.scatter(customer_metrics_df["Orders"],customer_metrics_df["Total Spent"], c=kmeans_4.labels_, alpha=0.3, s = 10)
plot.scatter(
    centroids_4[:, 0], 
    centroids_4[:, 2],
    marker ="X",
    s = 20,
    label = "Centroids"
)
plot.xlabel("Number of Orders")
plot.ylabel("Total Amount Spent")
plot.title("Orders vs Total Spent")
plot.legend()

print(kmeans_4.labels_)
print(centroids_4)

K2_df = customer_metrics_df.groupby("Cluster_2")[["Orders", "Total Quantity", "Total Spent"]].mean()
K2_df["Customers"] = customer_metrics_df["Cluster_2"].value_counts()

K4_df = customer_metrics_df.groupby("Cluster_4")[["Orders", "Total Quantity", "Total Spent"]].mean()
K4_df["Customers"] = customer_metrics_df["Cluster_4"].value_counts()

print(K2_df)
print(K4_df)
plot.show()