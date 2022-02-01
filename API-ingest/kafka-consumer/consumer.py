from ensurepip import bootstrap
from kafka import KafkaConsumer

#consumer = KafkaConsumer()

# Define a consumer that waits for new messages
def kafka_python_consumer():

    # Consumer using the topic name and setting a group id
    consumer = KafkaConsumer("ingestion-topic", group_id='mypthonconsumer', bootstrap_server='localhost:9092')
    for msg in consumer:
        print(msg)

print('start consuming')

# start the consumer
kafka_python_consumer()

print('done')