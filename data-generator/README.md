# Data-generator

`data-generator` app produce fake data in mysql, postgresql or kafka.
Use the data-generator app to produce continusly data in the sources and play with the other data services. 

## Model

kafka: messages in json
```
    customers: { 
                  "id": 1  
                 ,"name": "Gab"  
                 ,"age": 30 
               } 
    
    orders:    {  
                  "order_line_id": 1
                 ,"order_id": 1
                 ,"customer_id": 1 
                 ,"create_date": "2024-04-01 23:00:000" 
                 ,"productId": 1 
                 ,"amount": 100 
               } 
```
</br>
</br>

mysql: database mysql_data
```
    symbol (
        symbol varchar(100)
        category varchar(100)
        current_price decimal(18,2)
    )

    trades (
         symbol varchar(100)
        ,volume int
        ,side   char
    )
```

</br>
</br>

postgresql: database source_pg
```

    product (
         name      varchar(100)
        ,category  varchar(100)
        ,color     varchar(100)
        ,stock     int
    )

    sales (
         product     varchar(100)
        ,sales_date  datetime
        ,quantity    int
        ,unit_price  decimal(18,2)
    )

```

To run the python scripts activate the venv by running `. .venv/bin/activate` \
The folder `./events` contains methods that return the fake data 


`python_to_kafka.py` : produce json messages in topics `customers` and `orders`.
                       if the topics does not exists then it is create them.
`python_to_mysql_insert_customers.py`: insert data in table customers in mysql db
                       
