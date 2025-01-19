import os
from kafka import KafkaConsumer
from json import loads
import pickle
import pandas as pd
import numpy as np
import requests
import json
import psycopg2
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
schema_name = os.getenv("DB_SCHEMA")
table_name = os.getenv("DB_TABLE_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")



consumer = KafkaConsumer(
    'diabet_kafka_topic',
    bootstrap_servers=['host.docker.internal:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)


# def add_connection(text):
# """Connect Database POSTGRES."""
#     conn = psycopg2.connect(host=host, port = 5432, database = database,
#                             user=user, password=password)
#     cur=conn.cursor()
#     cur.execute("INSERT INTO ml_predict (predict) VALUES(%s)", (text,))
#     conn.commit()
#     conn.close()
#     cur.close()



if __name__ == '__main__':
    for message in consumer:
        message = message.value
        print(message)
        with open('model.pkl', 'rb') as f:
            model_forest = pickle.load(f)
        print(list(message.values()))
        print(np.array(list(message.values())))
        print(np.array(list(message.values())).reshape(1, -1))
        print(model_forest.predict(np.array(list(message.values())).reshape(1, -1)))

