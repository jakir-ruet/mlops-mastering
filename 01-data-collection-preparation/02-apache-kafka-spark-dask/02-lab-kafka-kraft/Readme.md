### Kafka KRaft - do this in 4 phases:

- Run Kafka in KRaft mode (Docker)
- Create topic
- Produce & consume messages (real-time)
- Test via UI + CLI
- (Bonus) Multi-broker cluster mindset

```bash
docker run --rm confluentinc/cp-kafka:7.5.0 kafka-storage random-uuid
```

> Should see `ptwX8oV7T4ueydBus5j0Ug`
> Add in Docker Composer just below `KAFKA_NODE_ID: 1`

```bash
CLUSTER_ID: ptwX8oV7T4ueydBus5j0Ug
```

```bash
docker-compose up -d
docker logs -f kafka-kraft
docker logs -f kafka-ui
```


#### Create Topic

```bash
docker exec -it kafka-kraft kafka-topics.sh \
--create \
--topic kafka-kraft \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

#### Check

```bash
docker exec -it kafka-kraft kafka-topics.sh \
--describe \
--topic kafka-kraft \
--bootstrap-server localhost:9092
```

#### Producer (Real-Time Input)

```bash
docker exec -it kafka-kraft kafka-console-producer.sh \
--topic kafka-kraft \
--bootstrap-server localhost:9092
```

> Type Messages

```bash
Hello Kafka
DevOps is awesome
Real-time streaming test
```

#### Consumer (Live Streaming)

```bash
docker exec -it kafka-kraft kafka-console-consumer.sh \
--topic kafka-kraft \
--bootstrap-server localhost:9092 \
--from-beginning
```

> You’ll see messages instantly = REAL-TIME STREAMING
