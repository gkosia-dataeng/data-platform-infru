# Data-generator

`data-generator` app produce fake data in mysql, postgresql or kafka.
Use the data-generator app to produce continusly data in the sources and play with the other data services. 

## Model

Topics in kafka or tables in databases
```
    customers: { 
                  "customerid": 1  
                 ,"name": "Gab"  
                 ,"age": 30 
                 ,"balance": 300
               } 
    

    orders:    {  
                  "customerid": 1
                 ,"create_date": "2024-04-01 23:00:000"
                 ,"productId": 1 
                 ,"amount": 100
                
               } 
```
</br>
</br>



#### To run the python scripts activate the venv by running `. .venv/bin/activate` \
The folder `./events` contains methods that return the fake data 


`python_to_kafka.py` : produce json messages in topics `customers` and `orders`.
                       If the topics does not exists then it is creating them. \
`python_to_mysql.py`: insert data in [mysql db](../mysql-maxwell/) \
`python_to_postgresql.py`: insert the data in [postgres db](../postgresql-kafkaconnect/)
                       
The schema from mysql and postgres databases is populated by the init file