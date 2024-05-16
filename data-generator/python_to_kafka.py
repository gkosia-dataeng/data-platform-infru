from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from events.customer import get_new_customer_event
from events.order import   get_order_event
import time
import random

__bootstrap_server = "localhost:9092"
__customers_topic = "customers"
__orders_topic    = "orders"

def post_to_kafka(producer, topic, customer_id, data):
    
    producer.send(topic, key= bytes(str(customer_id), 'utf-8'), value=data)

    producer.close()
    print("Posted to topic")

if __name__ == "__main__":
    

    kadminclient = KafkaAdminClient(bootstrap_servers = __bootstrap_server)

    topics = kadminclient.list_topics()

    if __customers_topic not in topics:
        kadminclient.create_topics(new_topics=[NewTopic(name=__customers_topic, num_partitions=1, replication_factor=1), NewTopic(name=__orders_topic, num_partitions=1, replication_factor=1)])

    customer_id = 1


    try:
        producer = KafkaProducer(bootstrap_servers = __bootstrap_server)
        post_to_kafka(producer, __customers_topic, customer_id, bytes(str(get_new_customer_event(customer_id)), 'utf-8'))
        
        while True:

            if random.randint(1,3) < 2 and customer_id < 50:
                customer_id+=1
                post_to_kafka(producer, __customers_topic, customer_id, bytes(str(get_new_customer_event(customer_id)), 'utf-8'))
            
            tmp_cust = random.randint(1,customer_id)
            for i in range(random.randint(0,8)):
                post_to_kafka(producer, __orders_topic, tmp_cust , bytes(str(get_order_event(tmp_cust)), 'utf-8'))
            
            time.sleep(random.randint(3,6))
    except Exception as e:
        print(str(e))
    finally:
        producer.close()