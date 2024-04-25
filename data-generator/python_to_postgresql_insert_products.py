import psycopg2
from events.product import get_product_info
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


# Function to insert records into the 'employees' table
def insert_records(connection, data):
    cursor = connection.cursor()

    # SQL query to insert records into the 'employees' table
    sql_query = "INSERT INTO public.product (id,name,category) VALUES (%s, %s, %s)"

    try:
        # Execute the query for each set of data
        cursor.executemany(sql_query, data)

        # Commit the changes
        connection.commit()
        print("Records inserted successfully")

    except Exception as e:
        # Rollback in case of an error
        connection.rollback()
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()




# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_config)


    product_id = 1
    insert_records(connection, get_product_info(product_id))
                   
    while True:

        if random.randint(1,3) < 2 and product_id < 20:
            product_id+=1
            insert_records(connection, get_product_info(product_id))
        
        time.sleep(random.randint(3,6))



except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    # Close the connection outside the try-except block
    if connection is not None:
        connection.close()
        print("PostgreSQL connection closed")
