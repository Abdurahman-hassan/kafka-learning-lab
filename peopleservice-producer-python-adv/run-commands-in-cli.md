## Install httpie (if not already installed)
```bash
brew install httpie
```

## Start the FastAPI server
```bash
uvicorn main:app --reload
```

## Make POST requests to create people

### Using httpie (http command):
```bash
# Create 3 people
http :8000/api/people count:=3

# Create 20 people
http :8000/api/people count:=20

# Create 30 people
http :8000/api/people count:=30
```

**Note:** The syntax is `http :8000/api/people count:=30` (not `count:=30/api/people`)

### Using curl (alternative if httpie is not installed):
```bash
# Create 3 people
curl -X POST "http://localhost:8000/api/people" \
  -H "Content-Type: application/json" \
  -d '{"count": 3}'

# Create 20 people
curl -X POST "http://localhost:8000/api/people" \
  -H "Content-Type: application/json" \
  -d '{"count": 20}'

# Create 30 people
curl -X POST "http://localhost:8000/api/people" \
  -H "Content-Type: application/json" \
  -d '{"count": 30}'
```

## Consumer (to see messages in Kafka)
```bash
# Replace 'people.adv.python' with your actual topic name from environment variables
docker exec -it cli-tools kafka-console-consumer \
  --bootstrap-server broker0:29092 \
  --topic people.adv.python
```

