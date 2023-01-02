from kafka import KafkaProducer
import uuid


producer = KafkaProducer(bootstrap_servers='localhost:9092')

for _ in range(10000):
    producer.send('foobar',key = uuid.uuid4().bytes, value = b'some_message_bytes1')
