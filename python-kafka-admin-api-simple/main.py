import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

logger = logging.getLogger()
load_dotenv(verbose=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - Kafka setup
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    topic = NewTopic(
        name=os.environ['TOPICS_PEOPLE_BASIC_NAME'],
        num_partitions=int(os.environ['TOPICS_PEOPLE_BASIC_PARTITIONS']),
        replication_factor=int(os.environ['TOPICS_PEOPLE_BASIC_REPLICAS'])
    )
    try:
        client.create_topics([topic])
    except TopicAlreadyExistsError:
        logger.warning("Topic already exists")
    finally:
        client.close()

    yield

    # Shutdown (cleanup if needed)


app = FastAPI(lifespan=lifespan)


# Add your endpoints
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

if os.getenv('ENABLE_MCP_HTTP', 'false').lower() == 'true':
    try:
        from fastapi_mcp import FastApiMCP
        mcp = FastApiMCP(app)
        mcp.mount_http()  # Mounts at /mcp by default
        logger.info("MCP HTTP endpoint enabled at /mcp (requires SSE)")
    except ImportError:
        logger.warning("fastapi-mcp not installed. Install it to enable HTTP MCP endpoint.")
    except Exception as e:
        logger.warning(f"Failed to enable MCP HTTP endpoint: {e}")
else:
    logger.info("MCP HTTP endpoint disabled (use mcp_server.py for stdio transport)")
