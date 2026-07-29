# Customer Behavior Analysis & Customer Segmentation

## Project Overview

This project is an analysis of a dataset from the UC Irvine Machine Learning Repository that tracked transactions for a United Kingdom based
online retail. Using python, the goal is to understand customer behavior and gather metrics. Using the results from the EDA, K-Means clustering is used
to establish whether the customers can be categorized based on their behaviors. Multiple K's were evaluated using the Elbow method and Silhouette score
to identify the best model, resulting in specific categories that encapusulates the customers in this data set.

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
  - [Customer Metrics](#customer-metrics)
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
- scikit_learn

## Data Cleaning

Before performing the analysis, I prepared the dataset by:
- Removing rows that had missing values.
- Removing columns that had information relevant to the analysis.
- Removing rows that had POSTCODE values of incomplete orders.
- Removing rows that had missing customer IDs

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


### Customer Metrics
Customer ID 12748 is the top returning customer, with a total of 209 orders.
Customer ID 14096 had the order with the most transactions.


### Visualizaitons

- Customer's Ordering Frequencys
 - This bar plot reveals how frequent customers order, with the great majority making less than 50 orders.

- Customer Total Spending
 - This histogram reveals that a majorty of the customers spend less than 500000.

- Orders vs Total Spent
 - Scatter plot reveals that customers tend to order less than 50 times, and spend less than 50000.

- Items vs Total Spent
 - Scatter plot reveals that customers tend to buy less than 25000 items and spend less than 50000.

- Orders vs Items
 - Scatter plot reveals that customers tend to order less than 50 times, and buy less than 25000 items.

- Orders vs Average Order Value
 - Scatter plot reveals that customers tend to order less than 50 times, and has an average order value of less than 10,000.

## Customer Segmentation


### Feature Selection
From the customer metrics dataframe, the features to choose from were Orders, Total Quality, Total Spent, and Average Order Value.
For the clustering, I picked features:  Orders, Total Quality, Total Spent, and Average Order Value. I left out Average Order Value because
it does not contribute new information to the analysis since it is a result of dividing Total Spent by Orders. 

### Data Preprocessing

Customer-level metrics were selected as features for clustering:
- Orders
- Total Quantity
- Total Spent

Because these features have different numerical ranges, they were standardized using StandardScaler before applying K-Means. 
Standardization ensured that each feature contributed equally to the distance calculations used by the clustering algorithm.


### Selecting the Number of Clusters

#### Elbow Method

#### Silhouette Score

### Final K-Means Model

### Cluster Summary

The elbow method and silhouette score were used to evaluate candidate values of K. Both K = 2 and K = 4 were investigated further. While K = 2 separated customers into broad low- and high-value groups, K = 4 revealed more detailed and interpretable purchasing behaviors.

The four customer segments differed in terms of purchase frequency, purchasing volume, and overall spending, providing a more informative representation of customer behavior.


### Cluster Visualizations

## Key Findings

- Customers make an average of 4 orders
- Customers spend an average of 2000
- Customers do purchase on average 1000 items
- Customers have a mean of 400 per order

## Conclusion
Most customers tend to make a few amount of orders, with a few being customers who had over 100 orders. Customers who 
had more orders tend to have more purchases and spending, with moderate correlations of 0.55. Customer segementation reveal there are four type of
customers, based on ordering frequency, total quantity, and total spending. 

## Current Limitations


## Future Improvements

