import pandas as pd

#Extract data from CSV's
customers=pd.read_csv("../data resources/customers.csv")
products=pd.read_csv("../data resources/products.csv")
orders=pd.read_csv("../data resources/orders.csv")

#Prints the top 5 rows
print('Customers: \n',customers.head())
print('Products: \n',products.head())
print('Orders: \n',orders.head())

#Clean customer names and cities
customers['name'] = customers['name'].str.title()
customers['city'] = customers['city'].str.title()
customers['join_date'] = pd.to_datetime(customers['join_date'])

#Ensure order_date is a valid date
orders['order_date'] = pd.to_datetime(orders['order_date'])

#Add derived columns
orders['average_price_per_item'] = orders['total_amount'] / orders['quantity']

#Join orders with products to include category
orders=orders.merge(products[['product_id','category']], on='product_id', how='left')

print('Customers: \n',customers.head())
print('Products: \n',products.head())
print('Orders: \n',orders.head())

#Load into Bigquery
from google.cloud import bigquery

client = bigquery.Client(project= 'rev-training07')


customer_table = "rev-training07.ecommerce_data.customers"
product_table = "rev-training07.ecommerce_data.products"
orders_table = "rev-training07.ecommerce_data.orders"

client.load_table_from_dataframe(customers,customer_table).result()
client.load_table_from_dataframe(products,product_table).result()
client.load_table_from_dataframe(orders,orders_table).result()

print("Data loaded successfully in BigQuery")
