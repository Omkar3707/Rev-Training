SELECT c.customer_id,c.name as customer_name,o.order_id,o.order_date,o.total_amount
From  `sales_data.customers` as c INNER JOIN `sales_data.orders` as o
ON c.customer_id = o.customer_id;

SELECT c.customer_id,c.name as customer_name,o.order_id,o.order_date
From  `sales_data.customers` as c LEFT JOIN `sales_data.orders` as o
ON c.customer_id = o.customer_id;

SELECT c.customer_id,c.name as customer_name,o.order_id,o.order_date
From  `sales_data.customers` as c RIGHT JOIN `sales_data.orders` as o
ON c.customer_id = o.customer_id;

SELECT c.customer_id,c.name as customer_name,o.order_id,o.order_date
From  `sales_data.customers` as c FULL OUTER  JOIN `sales_data.orders` as o
ON c.customer_id = o.customer_id;

SELECT c.name as customer_name,
p.name as product_name 
from `sales_data.customers` as c CROSS JOIN
`sales_data.products` as p;


SELECT
a.name as customer1,b.name as customer2,a.city
from `sales_data.customers` as a JOIN
`sales_data.customers` as b 
on a.city=b.city
AND a.customer_id <> b.customer_id;

SELECT o.order_id,
 p.name as product_name,
 p.category,
 o.quantity,
 o.total_amount
from `sales_data.orders` as o JOIN
`sales_data.products` as p
ON o.product_id = p.product_id
WHERE p.category = 'Electronics'; 


CREATE OR REPLACE TABLE `rev-training07.sales_data.customers_orders` AS
SELECT 
  c.customer_id,
  c.name,
  c.city,
  o.order_id,
  o.order_date,
  o.total_amount

FROM `rev-training07.sales_data.customers`  c
LEFT JOIN `rev-training07.sales_data.orders` o 
on c.customer_id=o.customer_id;


select * from `sales_data.customers_orders`;


CREATE OR REPLACE TABLE sales_data.sales_flattened AS

SELECT 

  o.order_id,

  o.order_date,

  o.quantity,

  o.total_amount,

  c.customer_id,

  c.name AS customer_name,

  c.city,

  p.product_id,

  p.name AS product_name,

  p.category,

  p.price 

FROM `sales_data.orders` AS o

JOIN `sales_data.customers` AS c ON o.customer_id = c.customer_id

JOIN `sales_data.products` AS p ON o.product_id = p.product_id;

 select * from `sales_data.sales_flattened`;


 CREATE OR REPLACE TABLE sales_data.orders_nested AS
SELECT 
  o.order_id,
  o.order_date,
  c.customer_id,
  c.name AS customer_name,
  ARRAY_AGG(STRUCT(p.product_id, p.name AS product_name, p.category, o.quantity,
o.total_amount)) AS items
FROM `sales_data.orders` AS o
JOIN `sales_data.customers` AS c ON o.customer_id = c.customer_id
JOIN `sales_data.products` AS p ON o.product_id = p.product_id
GROUP BY o.order_id, o.order_date, c.customer_id, c.name;
