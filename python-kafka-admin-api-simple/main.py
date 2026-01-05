import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from kafka import KafkaAdminClient
from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
from kafka.errors import TopicAlreadyExistsError

logger = logging.getLogger()
load_dotenv(verbose=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Kafka setup
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])

    # Create multiple topics
    topics = [
        NewTopic(
            name=os.environ['TOPICS_PEOPLE_BASIC_NAME'],
            num_partitions=int(os.environ['TOPICS_PEOPLE_BASIC_PARTITIONS']),
            replication_factor=int(os.environ['TOPICS_PEOPLE_BASIC_REPLICAS'])
        ),
        NewTopic(
            name=f"{os.environ['TOPICS_PEOPLE_BASIC_NAME']}-short",
            num_partitions=int(os.environ['TOPICS_PEOPLE_BASIC_PARTITIONS']),
            replication_factor=int(os.environ['TOPICS_PEOPLE_BASIC_REPLICAS']),
            topic_configs={
                'retention.ms': '360000'
            }
        ),
    ]

    # Create each topic
    for topic in topics:
        try:
            client.create_topics([topic])
        except TopicAlreadyExistsError:
            logger.warning(f"Topic {topic.name} already exists")

    # Update retention config for main topic
    cfg_resource_update = ConfigResource(
        ConfigResourceType.TOPIC,
        os.environ['TOPICS_PEOPLE_BASIC_NAME'],
        configs={'retention.ms': '360000'}
    )
    client.alter_configs([cfg_resource_update])

    client.close()

    yield

    # Shutdown (cleanup if needed)


app = FastAPI(lifespan=lifespan)


@app.get('/hello-world')
async def hello_world():
    return {"message": "Hello World!"}


@app.post('/people')
async def create_person(name: str, age: int):
    # Your logic here
    return {"name": name, "age": age, "status": "created"}


@app.get('/people')
async def get_people():
    # Your logic here
    return {"people": []}


# Optional: Enable MCP
if os.getenv('ENABLE_MCP_HTTP', 'false').lower() == 'true':
    try:
        from fastapi_mcp import FastApiMCP

        mcp = FastApiMCP(app)
        mcp.mount_http()  # Mounts at /mcp by default
        logger.info("MCP HTTP endpoint enabled at /mcp")
    except ImportError:
        logger.warning("fastapi-mcp not installed. Install it to enable HTTP MCP endpoint.")
    except Exception as e:
        logger.warning(f"Failed to enable MCP HTTP endpoint: {e}")
else:
    logger.info("MCP HTTP endpoint disabled (set ENABLE_MCP_HTTP=true to enable)")
