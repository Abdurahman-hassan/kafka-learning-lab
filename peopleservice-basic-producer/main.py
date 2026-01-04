
import os
import uuid
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from faker import Faker
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
from kafka.producer import KafkaProducer


from commands import CreatePeopleCommand
from entities import Person


load_dotenv(verbose=True)

app = FastAPI()

# this is the event that will be used to create the Kafka topic
@app.on_event('startup')
async def startup_event():
  # this is the Kafka admin client that will be used to create the Kafka topic
  client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
  # this is the topic that will be created
  try:
    # this is the topic that will be created
    topic = NewTopic(name=os.environ['TOPICS_PEOPLE_BASIC_NAME'],
                    num_partitions=int(os.environ['TOPICS_PEOPLE_BASIC_PARTITIONS']),
                    replication_factor=int(os.environ['TOPICS_PEOPLE_BASIC_REPLICAS']))
    # this is the topic that will be created
    client.create_topics([topic])
    # this is the error that will be raised if the Kafka topic already exists
  except TopicAlreadyExistsError as e:
    # this is the error that will be raised if the Kafka topic already exists
    print(e)
  # this is the finally block that will be used to close the Kafka admin client
  finally:
    client.close()


# this is the function that will be used to create the Kafka producer
def make_producer():
  # this is the Kafka producer that will be used to send the people to the Kafka topic
  producer = KafkaProducer(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
  return producer


# this is the endpoint for the POST /api/people endpoint
# it creates a list of people and sends them to the Kafka topic
@app.post('/api/people', status_code=201, response_model=List[Person])
async def create_people(cmd: CreatePeopleCommand):
  # this is the list of people that will be created
  people: List[Person] = []
  # this is the faker object that will be used to generate the people
  faker = Faker()
  # this is the producer that will be used to send the people to the Kafka topic
  producer = make_producer()

  # this is the loop that will be used to create the people
  for _ in range(cmd.count):
    # this is the person that will be created
    person = Person(id=str(uuid.uuid4()), name=faker.name(), title=faker.job().title())
    people.append(person)
    # this is the producer that will be used to send the person to the Kafka topic
    producer.send(topic=os.environ['TOPICS_PEOPLE_BASIC_NAME'],
                key=person.title.lower().replace(r's+', '-').encode('utf-8'),
                value=person.json().encode('utf-8'))

  # we use flush to ensure that the messages are sent to the Kafka topic
  producer.flush()

  # this is the list of people that will be returned
  return people
