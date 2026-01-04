## brew install httpie


## uvicorn main:app --reload                                    INT ✘ 
INFO:     Will watch for changes in these directories: ['/Users/abdelrahman/PycharmProjects/KafKa/peopleservice-basic-producer']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [39776] using WatchFiles
INFO:     Started server process [39778]
INFO:     Waiting for application startup.
[Error 36] TopicAlreadyExistsError: Request 'CreateTopicsRequest_v3(create_topic_requests=[(topic='people.basic.python', num_partitions=3, replication_factor=3, replica_assignment=[], configs=[])], timeout=30000, validate_only=False)' failed with response 'CreateTopicsResponse_v3(throttle_time_ms=0, topic_errors=[(topic='people.basic.python', error_code=36, error_message="Topic 'people.basic.python' already exists.")])'.
INFO:     Application startup complete.
INFO:     127.0.0.1:59231 - "POST /api/people/ HTTP/1.1" 307 Temporary Redirect
INFO:     127.0.0.1:59415 - "POST /api/people HTTP/1.1" 201 Created
INFO:     127.0.0.1:59529 - "POST /api/people HTTP/1.1" 201 Created
INFO:     127.0.0.1:59751 - "POST /api/people HTTP/1.1" 201 Created


## http :8000/api/people count:=3
HTTP/1.1 201 Created
content-length: 309
content-type: application/json
date: Sun, 04 Jan 2026 23:17:47 GMT
server: uvicorn

[
    {
        "id": "52c5108e-965c-454f-a95e-48a0450a40ee",
        "name": "Tanya Cabrera",
        "title": "Warehouse Manager"
    },
    {
        "id": "3970f768-abf3-4641-ab73-54d2f700ef0e",
        "name": "Rachel Campbell",
        "title": "Pensions Consultant"
    },
    {
        "id": "d65b65b8-c6c1-477e-93a7-fbb0bdee1f51",
        "name": "Elizabeth Hatfield",
        "title": "Commercial Horticulturist"
    }
]


## reciver
## docker exec -it cli-tools kafka-console-consumer --bootstrap-server broker0:29092 --topic people.basic.python
{"id":"cf4dde3b-6d2a-4aa8-9b93-893a37986006","name":"Theresa Sanders","title":"Geochemist"}
{"id":"9dc1518d-85e2-44c1-8633-eb6e1981da02","name":"Sandra Le","title":"Civil Service Administrator"}
{"id":"79fa4d91-2d1c-4ef8-9bfa-35a7157fb8fc","name":"Destiny Wyatt","title":"Biomedical Scientist"}
{"id":"d52a1df1-554b-46f6-86f0-ab84157864ae","name":"Sandra Flores","title":"Energy Manager"}
{"id":"edefac09-f78b-4f86-ba3d-72544deb405d","name":"Keith Foster","title":"Engineer, Automotive"}
{"id":"9162e282-2d82-425f-a90d-8287ad197310","name":"Jennifer Montgomery","title":"Teacher, Music"}
{"id":"d65b65b8-c6c1-477e-93a7-fbb0bdee1f51","name":"Elizabeth Hatfield","title":"Commercial Horticulturist"}
{"id":"52c5108e-965c-454f-a95e-48a0450a40ee","name":"Tanya Cabrera","title":"Warehouse Manager"}
{"id":"3970f768-abf3-4641-ab73-54d2f700ef0e","name":"Rachel Campbell","title":"Pensions Consultant"}


