import psycopg2
from events.customer import get_new_customer_info
from events.order import get_order_info
import random
import time

# Replace these with your actual PostgreSQL database credentials
db_config = {
    'host': 'localhost',
    'database': 'source_pg',
    'user': 'root',
    'password': 'root',
    'port': '5432',  # Usually 
}



def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        # Execute the query for each set of data
        cursor.executemany(query, [data])
        # Commit the changes
        connection.commit()
    except Exception as e:
        # Rollback in case of an error
        connection.rollback()
        print(f"Error: {e}, {data}, {query}")
    finally:
        # Close the cursor and connection
        cursor.close()

# Function to insert records into the 'users' table
def create_customer(connection, data):
    
    sql_query = "INSERT INTO public.customers (customerid, name, age, balance) VALUES (%s, %s, %s, %s)"
    execute_query(connection, sql_query, data)
    
def create_order(connection, data):

    sql_query = "INSERT INTO public.orders (customerid, create_date, productId, amount) VALUES (%s, %s, %s, %s)"
    execute_query(connection, sql_query, data)
    
def update_balance(connection, customer_id):
    sql_query = f"UPDATE public.customers SET balance = (SELECT SUM(amount) FROM public.orders WHERE customerid = {customer_id})"
    execute_query(connection, sql_query, None)



# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_config)

    customer_id = 1
    create_customer(connection, get_new_customer_info(customer_id))
                   
    while True:

        if random.randint(1,3) < 2 and customer_id < 50:
            customer_id+=1
            create_customer(connection, get_new_customer_info(customer_id))

        # create orders and update balance
        tmp_cust = random.randint(1,customer_id)
        num_of_orders = random.randint(0,8)
        for i in range(num_of_orders):
            create_order(connection, get_order_info(tmp_cust))

        if num_of_orders > 0:
            update_balance(connection, tmp_cust)

        time.sleep(random.randint(3,6))



except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    # Close the connection outside the try-except block
    if connection.is_connected():
        connection.close()
        print("PostgreSQL connection closed")
