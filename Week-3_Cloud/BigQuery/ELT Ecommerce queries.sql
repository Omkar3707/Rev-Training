CREATE SCHEMA IF  NOT EXISTS ecommerce_data;

create table `ecommerce_data.final_customers` as 
select
  customer_id,
  INITCAP(name) AS name,
  INITCAP(city) AS city,
  join_date
FROM `ecommerce_data.customers`;

select * from `ecommerce_data.final_customers`;

create table `ecommerce_data.final_products` as 
select
  product_id,
  INITCAP(name) AS name,
  INITCAP(category) AS category,
  price
FROM `ecommerce_data.products`;

select * from `ecommerce_data.final_products`;


create  or replace table  `ecommerce_data.final_orders` as 
select
  order_id,
  customer_id,product_id,
  order_date,
  quantity,total_amount,
  ROUND(total_amount / quantity,2) AS avg_price_per_item

FROM `ecommerce_data.orders`;

SELECT * from `ecommerce_data.final_orders`;

create or replace table `ecommerce_data.city_revunue` AS
SELECT 
 c.city,
 SUM(o.total_amount) AS total_revenue,
 COUNT(DISTINCT o.order_id) AS total_orders
FROM `ecommerce_data.final_orders` o
JOIN `ecommerce_data.customers` c
 ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;

SELECT * from `ecommerce_data.city_revunue`;

create or  replace table `ecommerce_data.top_products` AS 
SELECT
 p.name AS product_name,
 p.category,
 SUM(o.total_amount) AS total_sales
FROM  `ecommerce_data.orders` o  
JOIN `ecommerce_data.products` p
 ON o.product_id = p.product_id
GROUP BY product_name,category
ORDER BY total_sales DESC; 

SELECT * from `ecommerce_data.top_products`;

