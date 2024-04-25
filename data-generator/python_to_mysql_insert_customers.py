import mysql.connector
import random
from events.customer import get_new_customer_info
import time

# Replace these with your actual MySQL server and database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "mysql_data",
}


# Function to insert records into the 'users' table
def insert_records(connection, data):
    cursor = connection.cursor()

    # SQL query to insert records into the 'users' table
    sql_query = "INSERT INTO customers (id,name,age) VALUES (%s, %s, %s)"

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







# Connect to the MySQL server
try:
    connection = mysql.connector.connect(**db_config)

    customer_id = 1
    insert_records(connection, get_new_customer_info(customer_id))
                   
    while True:

        if random.randint(1,3) < 2 and customer_id < 50:
            customer_id+=1
            insert_records(connection, get_new_customer_info(customer_id))
        
        time.sleep(random.randint(3,6))



except Exception as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection outside the try-except block
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")