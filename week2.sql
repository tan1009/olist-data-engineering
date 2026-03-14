1) Which states have the most customers?

SELECT 
customer_state,
count(customer_id) as total_customers
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_customers.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by customer_state
ORDER by total_customers desc

This shows which state(SP) is generating the most revenue and we can target them more by giving them dsicounts and increasing revenue

2) Which cities have the most customers?

SELECT 
customer_city,
count(customer_id) as total_customers
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_customers.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by customer_city
ORDER by total_customers desc

This shows the city which has the most customers(sao paulo = 15540) and this gives us the insight the max we have reached in this city.

3) How many unique vs repeat customers?

SELECT 
count(DISTINCT customer_unique_id) as unique_customers,
count(customer_id) - count(DISTINCT customer_unique_id) as repeated_customers
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_customers.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers

Gives us how many customers are we able to retain and whats the success percentage.

4) How many orders per status?

SELECT 
count(order_id) as order_qty,
order_status
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_orders.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by order_status
ORDER by order_qty DESC

Gives us an oversight of the status and then we can find theb root cause of issues if they prevail.

5) Which months had the highest orders?

SELECT 
count(order_id) as order_qty,
month(order_purchase_timestamp) as month_number
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_orders.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by month(order_purchase_timestamp)
ORDER by order_qty DESC

We can see all the months and the orders in descending order shwoing us where we are strong and where we are falling short.

6)  Which year had more orders — 2017 or 2018?

SELECT 
count(order_id) as order_qty,
year(order_purchase_timestamp) as year_
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_orders.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by year(order_purchase_timestamp)
ORDER by order_qty DESC

7) How many orders were cancelled?

SELECT 
count(order_id) as order_qty,
order_status
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_orders.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
where order_status = 'canceled'
GROUP by order_status

8) What is total revenue?

SELECT 
SUM(price + freight_value) as total_revenue
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_items.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers

9) What is average order value?

SELECT 
avg(price) as avg_value
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_items.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers

10) What is total freight cost vs product revenue?

SELECT 
sum(price) as product_revenue,
sum(freight_value) as freight_cost
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_items.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers

11) Which sellers generate the most revenue?

SELECT 
sum(price) as product_revenue,
seller_id
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_items.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by seller_id
order by product_revenue DESC

12) Which product categories have the most products?

SELECT 
count(product_id) as product_qty,
product_category_name
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_products.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by product_category_name
order by product_qty DESC

13) What is the average product weight by category?

SELECT 
avg(product_weight_g) as avg_weight,
product_category_name
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_products.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by product_category_name
order by avg_weight DESC

14) Which category has the heaviest products?

SELECT 
max(product_weight_g) as max_weight,
product_category_name
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_products.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by product_category_name
order by max_weight DESC

15) What is the overall average review score?

SELECT 
avg(review_score) as avg_review_score
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_reviews.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers

16)  How many reviews per score (1,2,3,4,5)?

SELECT 
count(review_id) as review_count,
review_score
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_reviews.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
group by review_score
ORDER by review_count desc

17) Which months have the worst review scores?

SELECT 
month(review_creation_date) as month_number,
count(review_id) as bad_reviews
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_reviews.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
where review_score = '1'
group by month(review_creation_date)
ORDER by bad_reviews desc

18) Which payment method is most popular?

SELECT 
count(order_id) as order_qty,
payment_type
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_payments.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
GROUP by payment_type
order by order_qty desc 

19) What is the average payment installments?

SELECT 
AVG(payment_installments) as avg_installments
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_payments.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers


20) How many orders were paid in more than 6 installments?

SELECT 
count(order_id) as order_qty
FROM OPENROWSET(
    BULK 'https://olistdatalake11.dfs.core.windows.net/silver/cleaned_payments.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
) AS customers
where payment_installments>6

