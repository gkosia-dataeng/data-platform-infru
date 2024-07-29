import random
from datetime import datetime
import json

def get_order_info(customer_id):

    customerid = customer_id
    create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    productId   = random.choices(['A', 'B', 'C', 'D','E', 'F'])[0]
    amount = random.randrange(100,1000) / 100

    return (customerid, create_date, productId, amount,)


def get_order_event(customer_id):
    order = get_order_info(customer_id)

    event = {
         "customerid": order[0]
        ,"create_date": order[1]
        ,"productId": order[2]
        ,"amount": order[3]
    }

    return json.dumps(event)