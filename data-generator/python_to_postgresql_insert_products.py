import psycopg2

# Replace these with your actual PostgreSQL database credentials
db_config = {
    'host': 'localhost',
    'database': 'source_pg',
    'user': 'root',
    'password': 'root',
    'port': '5432',  # Usually 
}

# Sample data to insert into the 'employees' table
products_data = [
    (3,'banana','fruits'),
    (4,'powerbi','data'),
    (5,'pandas','data')
]

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

    # Insert records into the 'employees' table
    insert_records(connection, products_data)

except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    # Close the connection outside the try-except block
    if connection is not None:
        connection.close()
        print("PostgreSQL connection closed")
