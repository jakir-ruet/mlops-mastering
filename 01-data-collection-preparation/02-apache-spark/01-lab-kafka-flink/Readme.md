### Environment Setup

```bash
sudo yum update -y
sudo yum install -y python3
sudo yum install -y python3-pip
sudo apt install python3-venv -y
```

```bash
pip3 install fastapi uvicorn # Install FastAPI and Uvicorn
pip3 install kafka-python # Install Kafka
```

#### Kafka + Zookeeper (Docker Compose)

```bash
docker compose up -d
docker ps
docker compose down
```

```bash
http://localhost:8080/
```

#### Create a Topic

```bash
docker exec -it kafka kafka-topics \
  --create \
  --topic test-topic \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```

#### Start Producer

```bash
docker exec -it kafka kafka-console-producer \
  --topic test-topic \
  --bootstrap-server localhost:9092
```

```bash
Hello Kafka # Press Enter
Streaming data test # Press Enter
Real-time pipeline # Press Enter
```

#### Start Consumer (new terminal)

```bash
docker exec -it kafka kafka-console-consumer \
  --topic test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092
```

> **Should See**
> Hello Kafka
> Streaming data test
> Real-time pipeline

#### Describe Topic (CLI)

```bash
docker exec -it kafka kafka-topics \
  --describe \
  --topic test-topic \
  --bootstrap-server localhost:9092
```

```bash
docker exec -it kafka kafka-topics \
  --describe \
  --bootstrap-server localhost:9092
```
