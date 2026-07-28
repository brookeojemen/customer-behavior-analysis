# Customer Behavior Analysis

## Project Overview

This project is an analysis of a dataset from the UC Irvine Machine Learning Repository that tracked transactions for a United Kingdom based
online retail. Using python, the goal is to understand customer behavior and gather metrics. 

It answers questions like:
- **Which items are being bought the most?**
- **Which items are bringing in the most revenue?**
- **Who are returning customers? What is the probability a customer returns?** 


## Dataset

- **Dataset:** UC Irvine Machine Learning Repository
- **Source:** https://archive.ics.uci.edu/dataset/352/online+retail
- **Rows:** 396769 
- **Features:** 8

## Technologies Used

- Python
- Pandas
- Matplotlib

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



## Visualizaitons

## Customer's Ordering Frequencys
This bar plot reveals how frequent customers order, with the great majority making less than 50 orders.


## Customer Total Spending
This histogram reveals that a majorty of the customers spend less than 500000.

## Orders vs Total Spent
Scatter plot reveals that customers tend to order less than 50 times, and spend less than 50000.

## Items vs Total Spent
Scatter plot reveals that customers tend to buy less than 25000 items and spend less than 50000.

## Orders vs Items
Scatter plot reveals that customers tend to order less than 50 times, and buy less than 25000 items.

## Orders vs Average Order Value
Scatter plot reveals that customers tend to order less than 50 times, and has an average order value of less than 10,000.

## Key Findings

- Customers make an average of 4 orders
- Customers spend an average of 2000
- Customers do purchase on average 1000 items
- Customers have a mean of 400 per order

## Conclusion
Most customers tend to make a few amount of orders, with a few being customers who had over 100 orders. Customers who 
had more orders tend to have more purchases and spending, with moderate correlations of 0.55.

## Current Limitations


## Future Improvements

