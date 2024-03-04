from kafka import KafkaProducer
from device_event import generate_events
import time
import random
import uuid

__bootstrap_server = "localhost:9092"

def post_to_kafka(data):
    producer = KafkaProducer(bootstrap_servers = __bootstrap_server)
    producer.send('device-data', key= bytes(str(uuid.uuid4()), 'utf-8'), value=data)

    producer.close()
    print("Posted to topic")

if __name__ == "__main__":
    _offset = 10000

    while True:
        post_to_kafka(bytes(str(generate_events(offset=_offset)), 'utf-8'))
        time.sleep(random.randint(3,6))
        _offset+=1