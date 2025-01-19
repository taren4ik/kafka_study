from time import sleep
from json import dumps
import seaborn as sns

import pandas as pd
from kafka import KafkaProducer
from sklearn import datasets


def load_dataset():
    """Load dataset."""
    diabetes = datasets.load_diabetes(as_frame=True)
    return diabetes


producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

if __name__ == '__main__':
    for num in range(10):

        try:
            diabetes = load_dataset()
            data = dict(pd.DataFrame(diabetes['data']).iloc[num])
            producer.send('diabet_kafka_topic', value=data)
            print(f'Message {num} send successfully')
        except Exception as er:
            print(f'Error send message {er}: {str(num)}')
        sleep(10)
    producer.flush()
