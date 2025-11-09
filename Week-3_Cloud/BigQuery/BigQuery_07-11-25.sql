CREATE TABLE sales_data.customers AS
SELECT 'C001' AS customer_id, 'Arun Kumar' AS name, 'Chennai' AS city, DATE('2022-03-15') AS join_date UNION ALL
SELECT 'C002', 'Priya Sharma', 'Bangalore', DATE('2023-01-20') UNION ALL
SELECT 'C003', 'Rahul Mehta', 'Hyderabad', DATE('2022-07-10') UNION ALL
SELECT 'C004', 'Sneha Reddy', 'Pune', DATE('2023-06-25') UNION ALL
SELECT 'C005', 'Vikram Das', 'Mumbai', DATE('2024-02-12');


CREATE OR REPLACE TABLE sales_data.products AS
SELECT 'P101' AS product_id, 'Laptop' AS name, 'Electronics' AS category, 65000.0 AS price UNION ALL
SELECT 'P102', 'Smartphone', 'Electronics', 35000.0 UNION ALL
SELECT 'P103', 'Office Chair', 'Furniture', 9000.0 UNION ALL
SELECT 'P104', 'Bookshelf', 'Furniture', 7500.0 UNION ALL
SELECT 'P105', 'Wireless Mouse', 'Accessories', 1200.0;

CREATE OR REPLACE TABLE sales_data.orders AS
SELECT 'O001' AS order_id, 'C001' AS customer_id, 'P101' AS product_id, DATE('2024-05-12') AS order_date, 1 AS quantity, 65000.0 AS total_amount UNION ALL
SELECT 'O002', 'C002', 'P102', DATE('2024-05-18'), 2, 70000.0 UNION ALL
SELECT 'O003', 'C003', 'P103', DATE('2024-06-01'), 1, 9000.0 UNION ALL
SELECT 'O004', 'C001', 'P105', DATE('2024-06-10'), 3, 3600.0 UNION ALL
SELECT 'O005', 'C004', 'P104', DATE('2024-06-15'), 2, 15000.0 UNION ALL
SELECT 'O006', 'C005', 'P102', DATE('2024-07-02'), 1, 35000.0;


select * from sales_data.customers;

select*from `sales_data.products`;

select customer_id as CID, name as `Name of Cust`, join_date as DOJ
from `sales_data.customers` where join_date>'2022-03-15';

select customer_id as CID, name as `Name of Cust`, join_date as DOJ
from `sales_data.customers` where name like "%a%";

select customer_id as CID, name as `Name of Cust`, join_date as DOJ
from `sales_data.customers` where customer_id in ('C001','C002');

select customer_id as CID, name as `Name of Cust`, join_date as DOJ
from `sales_data.customers` where join_date between '2022-01-01' and '2025-01-01';

select customer_id as CID, name as `Name of Cust`, join_date as DOJ
from `sales_data.customers` where join_date>'2022-03-15' order by name;

select product_id,name,price,price*0.9 as discounted_price
from `sales_data.products`;

select customer_id as CID, name as `Name of Cust`, join_date as DOJ
from `sales_data.customers` where join_date>'2022-03-15' order by name limit 2;

select DISTINCT city from `sales_data.customers`;

select order_id,EXTRACT(year from order_date) as order_year
from `sales_data.orders`;

select order_id,EXTRACT(month from order_date) as order_month
from `sales_data.orders`;

select order_id,EXTRACT(day from order_date) as order_day
from `sales_data.orders`;

select count(*) as total_orders,
       sum(total_amount) as total_sales,
       avg(total_amount) as avg_order_value
from `sales_data.orders`;       

select customer_id, count(order_id) as num_of_orders,sum(total_amount) as total_spent
from `sales_data.orders` group by customer_id HAVING total_spent>20000;

select upper(name) as upper_name, length(name) as name_length
from `sales_data.customers`;