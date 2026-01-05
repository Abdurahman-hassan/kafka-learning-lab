**docker exec \-it cli-tools kafka-topics \--bootstrap-server broker0:29092 \--create \--topic people \--partitions
2 \-- replication-factor 2**

Created topic people.

That command is used to **create a new Kafka topic** named `people`.

Here is a breakdown of the command:

| Component                          | Meaning                                                                                                                 |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `docker exec -it cli-tools`        | Executes the following command inside a running Docker container named `cli-tools` in interactive mode (`-it`).         |
| `kafka-topics`                     | This is the main Kafka command-line utility for topic management.                                                       |
| `--bootstrap-server broker0:29092` | Specifies the address of the Kafka broker(s) to connect to (the entry point for the Kafka cluster).                     |
| `--create`                         | Tells the `kafka-topics` utility to create a new topic.                                                                 |
| `--topic people`                   | Specifies the name of the topic to be created, which is `people`.                                                       |
| `--partitions 2`                   | Configures the topic to have **2 partitions**. Partitions are how a topic's data is divided across brokers.             |
| `--replication-factor 2`           | Configures the topic so that each partition will have **2 replicas** (copies) on different brokers for fault tolerance. |

In summary, you are telling your Docker environment to run a Kafka utility that creates a topic named `people` with 2
partitions and a replication factor of 2\.

—------------

**docker exec \-it cli-tools kafka-topics \--bootstrap-server broker0:2**  
**9092 \--describe \--topic people**

Topic: people TopicId: p1zCLsTkQyeBW\_0kMb2gUw PartitionCount: 2 ReplicationFactor: 3 Configs: min.insync.replicas=2  
Topic: people Partition: 0 Leader: 2 Replicas: 2,1,0 Isr: 2,1,0  
Topic: people Partition: 1 Leader: 1 Replicas: 1,0,2 Isr: 1,0,2

The output you provided is the result of the `kafka-topics --describe --topic people` command, which shows the
configuration and partition status for the Kafka topic named `people`.

Here is a breakdown of what the different parts of the output mean:Topic Configuration Details

* **Topic: people**: The name of the Kafka topic.
* **TopicId: p1zCLsTkQyeBW\_0kMb2gUw**: A unique identifier for the topic.
* **PartitionCount: 2**: The topic is divided into 2 partitions (0 and 1).
* **ReplicationFactor: 3**: Each partition's data is copied and stored on 3 different brokers to ensure fault tolerance.
* **Configs: min.insync.replicas=2**: This is a configuration setting. It means that for a write operation (producer) to
  be considered successful, at least 2 replicas (including the leader) must have acknowledged the message.

Partition Status Details

The two following lines describe each of the topic's partitions:

| Field         | Partition 0 | Partition 1 | Meaning                                                                                                                                                                                      |
|---------------|-------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**     | people      | people      | The topic name.                                                                                                                                                                              |
| **Partition** | 0           | 1           | The unique ID of the partition.                                                                                                                                                              |
| **Leader**    | 2           | 1           | The ID of the broker currently responsible for all read/write requests for this partition. (Broker ID 2 for Partition 0, Broker ID 1 for Partition 1).                                       |
| **Replicas**  | 2, 1, 0     | 1, 0, 2     | The list of all brokers (by ID) that hold a replica of this partition, regardless of their status.                                                                                           |
| **Isr**       | 2, 1, 0     | 1, 0, 2     | **In-Sync Replicas.** The list of brokers (by ID) that are currently alive, caught-up with the leader, and eligible to be elected as the new leader. In this case, all replicas are in-sync. |

In summary, this output confirms that the `people` topic exists with 2 partitions, has a high availability setup with a
replication factor of 3, and all replicas are currently healthy and synchronized.

—----------

docker exec \-it cli-tools kafka-topics \--bootstrap-server broker0:29092 \--create \--topic pets

Created topic pets.

docker exec \-it cli-tools kafka-topics \--bootstrap-server broker0:29092 \--describe \--topic pets  
Topic: pets TopicId: EZT-F9sRSz-F9UJWTsP0Rw PartitionCount: 3 ReplicationFactor: 3 Configs: min.insync.replicas=2  
Topic: pets Partition: 0 Leader: 0 Replicas: 0,2,1 Isr: 0,2,1  
Topic: pets Partition: 1 Leader: 2 Replicas: 2,1,0 Isr: 2,1,0  
Topic: pets Partition: 2 Leader: 1 Replicas: 1,0,2 Isr: 1,0,2

—------

exec \-it cli-tools kafka-topics \--bootstrap-server broker0:29092 \--delete \--topic pets  
—----

