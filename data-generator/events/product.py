import random
import json

def get_product_info(id):

    product_id = id
    category = random.choices('ABCDE')
    name = category + "_" + random.choices('abcdefghijklmnopqrstuvwxyz')
    

    return (product_id, name, category)


def get_product_event(product_id):
    product = get_product_info(product_id)

    event = {
         "product_id": product[0]
        ,"name": product[1]
        ,"category": product[2]
      
    }

    return json.dumps(event)