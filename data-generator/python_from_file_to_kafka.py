from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import time
import random
import logging


logging.basicConfig(level=logging.INFO)


__bootstrap_server = "localhost:9092"


def post_to_kafka(producer, topic, key, data):
    
    producer.send(topic, key= bytes(str(key), 'utf-8'), value=data)
    print("Posted to topic")


def load_messages(file):

    with open(file, 'r') as f:
        
        topics  = set()
        messages = []
        for line in f:
            if '@' in line:
                topic, message = line.split('@')
                topics.add(topic)
                messages.append({'topic': topic, "message": message})
                logging.info(f"readed topic: {topic}, message: {message}")

        return topics, messages
                

if __name__ == "__main__":
    

    kadminclient = KafkaAdminClient(bootstrap_servers = __bootstrap_server)

    topics, messages = load_messages('./events/messages_enrichStream.txt') 

    existing_topics = kadminclient.list_topics()

    for topic in topics:
        if topic not in existing_topics:
            logging.info(f"creating topic {topic}")
            kadminclient.create_topics(new_topics=[NewTopic(name=topic, num_partitions=1, replication_factor=1)])

    try:
        producer = KafkaProducer(bootstrap_servers = __bootstrap_server)
        for message in messages:
            post_to_kafka(producer, message['topic'], 1, bytes(message['message'], 'utf-8'))
            logging.info(f"producing to {message['topic']}, message {message['message']}")
    except Exception as e:
        logging.error(str(e))
    finally:
        producer.close()