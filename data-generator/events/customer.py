from faker import Faker
import random
import json


def get_new_customer_info(id):
    
    f = Faker()
    name = f.name()
    age = random.randint(18,85)
    initial_balance = 1000

    return (id,name,age, initial_balance,)


def get_new_customer_event(id):

    info = get_new_customer_info(id)

    event =  {
         "customerid": info[0]
        ,"name": info[1]
        ,"age": info[2]
        ,"balance": info[3]

    }

    
    return json.dumps(event)