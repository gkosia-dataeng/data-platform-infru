import random
from datetime import datetime
import json

def get_order_info(customer_id):

    order_customer_id = customer_id
    create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    product     = random.choices(['A', 'B', 'C', 'D'])
    amount = random.randrange(100,1000) / 100

    return (order_customer_id, create_date, product, amount)


def get_order_event(customer_id):
    order = get_order_info(customer_id)

    event = {
         "order_customer_id": order[0]
        ,"create_date": order[1]
        ,"productId": order[2]
        ,"amount": order[3]
    }

    return json.dumps(event)