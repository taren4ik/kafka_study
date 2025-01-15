from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['host.docker.internal:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

if __name__ == '__main__':
    for e in range(5):
        data = {'number': e}
        try:
            producer.send('first_kafka_topic', value=data)
            print(f'Message {e} send successfully')
        except Exception as er:
            print(f'Error send message {er}: {str(e)}')
        sleep(5)
    producer.flush()
