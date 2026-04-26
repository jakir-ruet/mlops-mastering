### Apache Spark (PySpark)

Apache Spark is a distributed data processing engine designed for **big data workloads**.

#### Key idea

- Processes data across multiple machines (cluster computing)
- Uses lazy execution (builds a plan first, runs later)
- Optimized for very large-scale data (TBs → PBs)

### Dask

Dask is a parallel computing library for Python that scales pandas-like workflows.

#### Key idea

- Works on single machine or cluster
- Extends pandas, NumPy, and scikit-learn style APIs
- More “Python-native” than Spark

#### Spark vs Dask

| Feature        | Spark (PySpark)      | Dask                      |
| -------------- | -------------------- | ------------------------- |
| Scale          | Huge (PB-level)      | Medium–Large              |
| Setup          | Complex cluster      | Simple (local or cluster) |
| API style      | SQL + DataFrame      | Pandas-like               |
| Performance    | Very strong at scale | Good for Python workflows |
| Learning curve | Higher               | Lower                     |
| Use case       | Big data engineering | Data science + ML scaling |

### Apache Kafka (Data Streaming Backbone)

Apache Kafka is a distributed event streaming platform. It's `High-speed messaging system for real-time data pipelines`. It continuously collects, stores, and forwards data streams.

#### How Kafka works

1. Producer → sends data
   Mobile app sends click events → Bank sends transaction logs.
2. Topic → storage channel
   Like a category (e.g., payments, logs, clicks)
3. Consumer → reads data
   Analytics system → ML model → Monitoring system

### Apache Flink (Stream Processing Engine)

Apache Flink is a real-time stream processing framework. Kafka collects data → Flink processes it instantly. Flink is where the actual computation happens in real time.

#### What Flink does

- Real-time analytics
- Filtering, aggregation
- Window-based processing (e.g., last 5 minutes data)
- Stateful stream processing
- Event-time processing

### Kafka vs Flink

| Feature  | Kafka                    | Flink                  |
| -------- | ------------------------ | ---------------------- |
| Role     | Data streaming pipeline  | Data processing engine |
| Function | Collect + transport data | Analyze + compute data |
| Type     | Message broker           | Stream processor       |
| Storage  | Yes (log-based)          | No (processing only)   |
| Speed    | Very fast ingestion      | Real-time computation  |
