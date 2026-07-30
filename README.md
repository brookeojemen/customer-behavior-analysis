# Customer Behavior Analysis & Customer Segmentation

## Project Overview

This project is an analysis of a dataset from the UC Irvine Machine Learning Repository that tracked transactions for a United Kingdom based
online retail. Using python, the goal is to understand customer behavior and gather metrics. Using the results from the EDA, K-Means clustering is used
to establish whether the customers can be categorized based on their behaviors. Multiple K's were evaluated using the Elbow method and Silhouette score
to identify the best model, resulting in four customer segments that represent distinct purchasing behaviors.

It answers questions like:
    - **Which products are being bought most frequently?**
    - **Which products generate the most revenue?**
    - **How often do customers return?**
    - **Can customers be grouped into distinct purchasing segments based on their behavior?**

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Data Cleaning](#data-cleaning)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Product Analysis](#product-analysis)
  - [Customer Behavior Analysis](#customer-behavior-analysis)
  - [Visualizations](#visualizations)
- [Customer Segmentation](#customer-segmentation)
  - [Feature Selection](#feature-selection)
  - [Data Preprocessing](#data-preprocessing)
  - [Selecting the Number of Clusters](#selecting-the-number-of-clusters)
    - [Elbow Method](#elbow-method)
    - [Silhouette Score](#silhouette-score)
  - [Final K-Means Model](#final-k-means-model)
  - [Cluster Summary](#cluster-summary)
  - [Cluster Visualizations](#cluster-visualizations)
- [Key Findings](#key-findings)
- [Conclusion](#conclusion)
- [Current Limitations](#current-limitations)
- [Future Improvements](#future-improvements)

## Dataset

- **Dataset:** UC Irvine Machine Learning Repository
- **Source:** https://archive.ics.uci.edu/dataset/352/online+retail
- **Rows:** 396769 
- **Features:** 8

## Technologies Used

- Python 
- Pandas 
- Matplotlib
- scikit-learn

## Data Cleaning

Before performing the analysis, I prepared the dataset by:
- Removing rows that had missing values.
- Removing columns that had information relevant to the analysis.
- Removing rows with StockCode values (POST, DOT, and D) that represent non-product transactions or incomplete orders.
- Removing rows that had missing customer IDs.

The analysis focuses primarily on:

- Customer ID
- Unit Price
- Invoice Number
- Stock Code
- Quantity

---

## Exploratory Data Analysis

### Product Analysis
 I first found out what the most popular item was, and which item was making the most revenue. 


### Customer Behavior Analysis
- Customer ID 12748 is the top returning customer, with a total of 209 orders.
- Customer ID 14096 had the order with the most transactions.
- Most customers placed fewer than 50 orders
- Orders and total spending showed a moderate positive correlation (0.55).


### Visualizaitons

- Customer Ordering Frequency
 - This bar plot reveals how frequent customers order, with the great majority making less than 50 orders.

- Customer Total Spending
 - This histogram reveals that a majority of the customers spend less than 500000.

- Orders vs Total Spent
 - Scatter plot reveals that customers tend to order less than 50 times, and spend less than 50000.

- Items vs Total Spent
 - Scatter plot reveals that customers tend to buy less than 25000 items and spend less than 50000.

- Orders vs Items
 - Scatter plot reveals that customers tend to order less than 50 times, and buy less than 25000 items.

- Orders vs Average Order Value
 - Scatter plot reveals that customers tend to order less than 50 times, and have an average order value less than 10,000.

## Customer Segmentation


### Feature Selection
From the customer metrics dataframe, the features to choose from were Orders, Total Quantity, Total Spent, and Average Order Value.
For the clustering, I picked features:  Orders, Total Quantity, and Total Spent. I left out Average Order Value because
it does not contribute new information to the analysis since it is a result of dividing Total Spent by Orders. 

### Data Preprocessing

Customer-level metrics were selected as features for clustering:
- Orders
- Total Quantity
- Total Spent

Because these features have different numerical ranges, they were standardized using StandardScaler before applying K-Means. 
Standardization ensured that each feature contributed equally to the distance calculations used by the clustering algorithm.


### Selecting the Number of Clusters

I used the Elbow Method and Silhouette score to determine the best value for K to use for KMeans. 


#### Elbow Method

The Elbow Method was used by plotting inertia against the number of clusters (K). Inertia measures the total distance between each data point and 
the centroid of its assigned cluster. As the number of clusters increases, inertia decreases because the clusters become more specific.

The elbow plot showed that the reduction in inertia began to level off around K = 4, indicating that adding additional clusters beyond four resulted in diminishing improvements to the clustering solution.

#### Silhouette Score

The Silhouette Score was calculated for values of K ranging from 2 to 10. It measures how similar each customer is to its assigned cluster compared to other clusters.
Higher silhouette scores indicate better-defined clusters.

The highest silhouette score occurred at **K = 2**, suggesting that two clusters produced the strongest overall separation.

### Final K-Means Model

Because the two methods were not in agreement, I made plots for both to help determine which model better categorizes the customers. Although K = 2 produced the highest silhouette score, 
K = 4 created more meaningful and interpretable customer groups based on purchasing frequency, purchase quantity, and total spending. Therefore, K = 4 was 
selected as the final clustering model.

### Cluster Summary

The elbow method and silhouette score were used to evaluate candidate values of K. Both K = 2 and K = 4 were investigated further. While K = 2 separated 
customers into broad low- and high-value groups, K = 4 revealed more detailed and interpretable purchasing behaviors.

The four customer segments differed in terms of purchase frequency, purchasing volume, and overall spending, providing a more informative representation of customer behavior.

### Cluster Visualizations
 -**Orders vs. Total Quantity (K = 2)**
 ![alt text](<images/Orders vs Items - K=2.png>)

 This visualization shows that K = 2 separates customers into distinct purchasing groups based on ordering frequency and purchase volume.

 -**Orders vs. Total Spent (K = 2)**
 ![alt text](<images/Orders vs Total Spent - K=2.png>)

 This visualization shows that K = 2 separates customers into distinct purchasing groups based on ordering frequency and total spending.

 -**Orders vs. Total Quantity (K = 4)**
 ![alt text](<images/Orders vs Items - K=4.png>)

This visualization shows that K = 4 separates customers into distinct purchasing groups based on ordering frequency and purchase volume.

 -**Orders vs. Total Spent (K = 4)**
 ![alt text](<images/Orders vs Total Spent - K=4.png>)

  This visualization shows that K = 4 separates customers into distinct purchasing groups based on ordering frequency and total spending.


## Key Findings

- The most frequently purchased product was StockCode 85123A.
- Customer 12748 was the most frequent purchaser with 209 orders.
- Most customers placed fewer than 50 orders.
- Orders and spending showed a moderate positive relationship.
- K-Means clustering identified four distinct customer purchasing segments.

## Conclusion

The analysis showed that most customers place relatively few orders, while a small number of customers account for a disproportionate share of purchases and spending. 
Exploratory data analysis revealed purchasing trends and customer behavior, while K-Means clustering identified four meaningful customer segments based on 
ordering frequency, purchase quantity, and total spending. These findings provide insight into customer purchasing patterns and demonstrate how unsupervised 
machine learning can be used to support customer segmentation.

## Current Limitations
- The clustering model only used purchasing behavior metrics.
- Excluded Customer geographic and date information
- Analysis does not take into consideration of changes in customer behavior

## Future Improvements

- Develop a model to predict future customer purchasing behavior
- Consider the impact of geography and date of invoices
- Use other clustering algorithms
- Incorporate the Recency metric alongside the existing Frequency and Monetary metrics to build a complete RFM customer segmentation framework. 