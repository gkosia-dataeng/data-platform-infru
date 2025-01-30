import sys
from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes, Schema, FormatDescriptor, TableDescriptor

def start_the_steam():

    # Initialize the Table Environment
    env_settings = EnvironmentSettings.in_streaming_mode()
    t_env = TableEnvironment.create(env_settings)

    # topic a
    t_env.execute_sql("""CREATE TABLE topica (
        user_id INT,
        name STRING,
        update_time TIMESTAMP(3),
        WATERMARK FOR update_time AS update_time - INTERVAL '5' SECOND,
        PRIMARY KEY(user_id) NOT ENFORCED
    ) WITH (
        'connector' = 'upsert-kafka',
        'topic' = 'test-source-atopic',
        'properties.bootstrap.servers' = 'kafka:19092',
        'value.format' = 'json',
        'key.format' = 'json',
        'properties.group.id' = 'test-group'
    )
    """)


    # topic b
    t_env.execute_sql("""CREATE TABLE topicb (
        user_id INT,
        totalProfit DOUBLE,
        create_date TIMESTAMP(3),
        WATERMARK for create_date AS create_date - INTERVAL '5' SECOND
                      
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'test-source-btopic',
        'properties.bootstrap.servers' = 'kafka:19092',
        'value.format' = 'json',
        'properties.group.id' = 'test-group',
        'scan.startup.mode' = 'earliest-offset'
    )
    """)

    SELECT *
    FROM topicb  as b
    LEFT JOIN topica FOR SYSTEM_TIME AS OF b.create_date  as a
       ON b.user_id = a.user_id;
    

    {"user_id": 2}/{"user_id": 2, "name": "gab", "update_time" : "2025-01-01 10:30:00"}

    {"user_id": 2}/{"user_id": 2, "name": "zac", "update_time" : "2025-01-01 10:26:30"}
    

    {"user_id": 2, "totalProfit": 20.2, "create_date": "2025-01-01 10:32:00"}
    , 
    # sink
    t_env.execute_sql("""CREATE TABLE sink (
        user_id INT PRIMARY KEY NOT ENFORCED,
        name STRING,
        totalProfit DOUBLE
    ) WITH (
        'connector' =  'upsert-kafka',
        'topic' = 'test-sink-topic',
        'properties.bootstrap.servers' = 'kafka:19092',
        'key.format' = 'json',
        'value.format' = 'json'
                      
    )
    """)


    t_env.execute_sql("""
        INSERT INTO sink
        SELECT a.user_id
              ,a.name
              ,b.totalProfit
        FROM topica a
        LEFT JOIN topicb b
          ON a.user_id = b.user_id
    """)

if __name__ == '__main__':
    
    start_the_steam()