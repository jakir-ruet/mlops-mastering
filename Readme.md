## More About Me – [Take a Look!](http://www.mjakaria.me)

### MLOps

MLOps (Machine Learning Operations) is a set of practices that combines Machine Learning (ML) and DevOps to automate, deploy, monitor, and manage machine learning models in production reliably and efficiently. It focuses on the full lifecycle:

- Data collection
- Model training
- Testing & validation
- Deployment
- Monitoring & retraining

### MLOps Engineer

An MLOps Engineer is responsible for making ML models production-ready, scalable, and reliable. Think of it like:

- `Data Scientist` → `builds model`
- `MLOps Engineer` → `makes it work in real-world systems`

#### Role & Responsibilities of an MLOps Engineer

| #   | Area                      | Key Responsibilities                                                                                                                  | Tools/Technologies                          |
| --- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| 1   | Model Deployment          | Deploy ML models as APIs and services; containerize using Docker; orchestrate with Kubernetes; build CI/CD pipelines for ML workflows | Docker, Kubernetes, GitHub Actions, Jenkins |
| 2   | Automation                | Automate end-to-end ML pipelines including training, testing, and deployment; schedule and manage workflows                           | Apache Airflow, Kubeflow                    |
| 3   | Data & Model Versioning   | Track dataset versions and model versions; manage reproducibility of experiments                                                      | DVC, MLflow                                 |
| 4   | Monitoring                | Monitor model performance (accuracy, drift); track system metrics like latency and errors; ensure reliability in production           | Prometheus, Grafana                         |
| 5   | Infrastructure Management | Manage scalable infrastructure on cloud platforms; handle compute resources (CPU/GPU); optimize cost and performance                  | AWS, GCP, Azure                             |

#### MLOps vs DevOps

| Feature    | DevOps                 | MLOps                            |
| ---------- | ---------------------- | -------------------------------- |
| Focus      | Application code       | ML models + data                 |
| Input      | Source code            | Code + Data                      |
| Output     | Software app           | Trained ML model                 |
| Testing    | Unit/Integration tests | Model validation, accuracy       |
| Deployment | App deployment         | Model deployment                 |
| Monitoring | Logs, uptime           | Accuracy + drift + performance   |
| Complexity | Medium                 | Higher (data changes constantly) |

### MLOps Lifecycle (End-to-End)

![MLOps Lifecycle](/img/mlops-lifecycle.png)

| #   | Stage             | Description                                  | Key Activities                                    | Tools/Technologies                    |
| --- | ----------------- | -------------------------------------------- | ------------------------------------------------- | ------------------------------------- |
| 1   | Data Collection   | Gather raw data from various sources         | Data ingestion, APIs, databases, logs             | SQL, APIs, data pipelines             |
| 2   | Data Preparation  | Clean and transform data for training        | Data cleaning, feature engineering, normalization | pandas, NumPy                         |
| 3   | Model Development | Build and train ML models                    | Algorithm selection, training, tuning             | scikit-learn, TensorFlow, PyTorch     |
| 4   | Model Evaluation  | Validate model performance before deployment | Accuracy check, validation, testing               | Metrics (accuracy, precision, recall) |
| 5   | Model Versioning  | Track models and datasets                    | Version control, experiment tracking              | MLflow, DVC                           |
| 6   | Deployment        | Deploy model to production environment       | API creation, containerization, CI/CD             | Docker, Kubernetes                    |
| 7   | Monitoring        | Track performance of deployed model          | Drift detection, latency, error monitoring        | Prometheus, Grafana                   |
| 8   | Retraining        | Update model with new data                   | Continuous training, pipeline automation          | Apache Airflow, Kubeflow              |
| 9   | Governance        | Ensure compliance and control                | Security, access control, audit logs              | IAM, policies, model governance tools |

### MLOps Tools & Their Uses

| Category                           | Purpose                                          | Tools                                           | Use (What They Actually Do)                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------- | --------------------------------------------------------------- |
| **Data Processing**                | Clean, transform, and prepare data for ML models | pandas, NumPy, Spark                            | Data cleaning, feature engineering, large-scale data processing |
| **Model Development**              | Build and train machine learning models          | scikit-learn, TensorFlow, PyTorch               | Model training, evaluation, and algorithm development           |
| **Experiment Tracking**            | Track experiments, parameters, and results       | MLflow, Weights & Biases, Neptune               | Log metrics, compare experiments, reproduce results             |
| **Data & Model Versioning**        | Version control for datasets and models          | DVC, Git                                        | Track dataset/model changes and ensure reproducibility          |
| **CI/CD**                          | Automate testing, building, and deployment       | Jenkins, GitHub Actions, GitLab CI/CD, CircleCI | Automate ML pipeline validation and deployment                  |
| **Containerization**               | Package ML applications for portability          | Docker                                          | Create portable ML environments                                 |
| **Orchestration**                  | Manage containerized applications at scale       | Kubernetes, Argo CD                             | Deploy, scale, and manage ML workloads                          |
| **Workflow Automation**            | Automate ML pipelines (ETL → Train → Deploy)     | Apache Airflow, Kubeflow, Luigi                 | Schedule and manage end-to-end ML workflows                     |
| **Model Serving**                  | Deploy models as APIs for real-time inference    | FastAPI, TensorFlow Serving                     | Expose ML models as production APIs                             |
| **Monitoring & Logging**           | Track performance, detect drift, system health   | Prometheus, Grafana, ELK Stack                  | Monitor models, logs, and infrastructure health                 |
| **Security & Compliance**          | Ensure secure and compliant ML systems           | Snyk, SonarQube                                 | Vulnerability scanning, code quality checks                     |
| **Cloud Platforms**                | Provide scalable ML infrastructure               | AWS, Azure, GCP                                 | Hosting, compute, storage, managed ML services                  |
| **Automated Testing & Validation** | Ensure data/model quality before deployment      | TFX, Great Expectations                         | Validate datasets, pipelines, and model behavior                |
| **Hyperparameter Tuning**          | Optimize model performance automatically         | Optuna, Hyperopt                                | Automated search for best model parameters                      |

> Simple Flow `Data → Train → Evaluate → Deploy → Monitor → Retrain → Repeat`

### MLOps Architecture

![MLOps Architecture](/img/mlops-architecture.png)

MLOps architecture encompasses the `infrastructure`, `automation`, and `governance` layers that make that lifecycle repeatable and scalable. Think of MLOps as the `bridge` between `Data Science` (building models) and `DevOps` (shipping software). Here is the comprehensive breakdown of a full MLOps architecture.

#### The Core Functional Pillars

| Stage | Full Form                        | Purpose                                                                     | Key Activities                                                       | Tools                   |
| ----- | -------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------- |
| CI    | Continuous Integration           | Ensure code and ML pipeline changes are integrated and tested automatically | Code commit, unit tests, data validation, model training trigger     | GitHub Actions, Jenkins |
| CD    | Continuous Deployment / Delivery | Automatically deploy ML models to production                                | Build Docker image, deploy API, rollout updates (blue/green, canary) | Docker, Kubernetes      |
| CT    | Continuous Training              | Automatically retrain models when new data arrives or performance drops     | Data ingestion, retraining, validation, model versioning             | MLflow, Apache Airflow  |
| CM    | Continuous Monitoring            | Continuously monitor model and system performance in production             | Accuracy tracking, drift detection, latency monitoring, alerts       | Prometheus, Grafana     |

> Continuous Integration (CI), Continuous Deployment (CD), Continuous Training (CT), Continuous Monitoring (CM)

### Data Collection and Preparation

| Stage               | Sub-Step            | Description                           | Example                | Tools              |
| ------------------- | ------------------- | ------------------------------------- | ---------------------- | ------------------ |
| **Data Collection** | Data Sources        | Gather raw data from multiple systems | DB, APIs, logs, IoT    | MySQL, APIs, Kafka |
|                     | Batch Ingestion     | Collect data at intervals             | Daily sales report     | Airflow, Cron      |
|                     | Real-time Ingestion | Continuous streaming data             | Fraud detection stream | Kafka, Kinesis     |
|                     | Data Storage        | Store raw data                        | Data lake/warehouse    | S3, BigQuery, HDFS |
|                     | Data Validation     | Ensure data correctness               | Schema checks          | Great Expectations |

| Stage                | Sub-Step            | Description                            | Example             | Tools          |
| -------------------- | ------------------- | -------------------------------------- | ------------------- | -------------- |
| **Data Preparation** | Data Cleaning       | Fix missing, duplicate, incorrect data | Fill salary NULL    | Pandas         |
|                      | Data Transformation | Convert data into usable format        | Normalize values    | Scikit-learn   |
|                      | Feature Engineering | Create new useful features             | Age → age group     | Pandas, Spark  |
|                      | Encoding            | Convert categorical → numeric          | Country → One-Hot   | OneHotEncoder  |
|                      | Scaling             | Normalize numerical data               | Salary scaling      | StandardScaler |
|                      | Data Reduction      | Remove unnecessary data                | Drop unused columns | Pandas         |
|                      | Data Splitting      | Train/Test split                       | 80/20 split         | Scikit-learn   |

> Data Sources → Ingestion → Storage → Cleaning → Transformation → Feature Engineering → Split → ML Model

**Key Insight**

| Area             | Focus                               |
| ---------------- | ----------------------------------- |
| Data Collection  | Getting **correct & complete data** |
| Data Preparation | Making data **clean & ML-ready**    |

#### Data Storage in an Organization

| Storage Type              | Purpose                     | Data Type                 | Example Technologies |
| ------------------------- | --------------------------- | ------------------------- | -------------------- |
| **Operational DB (OLTP)** | Run daily applications      | Structured                | MySQL, PostgreSQL    |
| **Data Warehouse (OLAP)** | Analytics & reporting       | Structured                | Snowflake, BigQuery  |
| **Data Lake**             | Store raw data (any format) | Structured + Unstructured | S3, HDFS             |
| **Feature Store**         | ML-ready features           | Processed data            | Feast                |
| **Backup Storage**        | Disaster recovery           | All                       | S3 Glacier, Tape     |

#### Data Ingestion vs ETL

| Aspect     | Data Ingestion             | ETL (Extract, Transform, Load)      |
| ---------- | -------------------------- | ----------------------------------- |
| Purpose    | Bring data into the system | Clean, transform, and organize data |
| Focus      | Data movement              | Data processing                     |
| Steps      | Collect → Store            | Extract → Transform → Load          |
| Complexity | Simple to moderate         | Moderate to complex                 |
| Timing     | Batch or real-time         | Mostly batch (can be streaming)     |
| Output     | Raw data                   | Clean, structured data              |
| Use Case   | Logging, streaming events  | Analytics, ML training              |
| Tools      | Kafka, Kinesis, NiFi       | Airflow, Spark, Talend              |

#### Work Flow Together

`Data Sources → Data Ingestion (collect & store raw data) → ETL Process (clean + transform) → Data Warehouse/Feature Store → ML Model/Analytics`

> Key Insight
>
> - Data Ingestion = Moving data
> - ETL = Making data usable

#### Data Cleaning vs Data Transformation

| Aspect           | Data Cleaning                      | Data Transformation              |
| ---------------- | ---------------------------------- | -------------------------------- |
| Goal             | Fix bad or dirty data              | Convert data into usable format  |
| Focus            | Accuracy & quality                 | Structure & representation       |
| Problems handled | Missing values, duplicates, errors | Scaling, encoding, normalization |
| Input            | Raw data                           | Cleaned data                     |
| Output           | Clean dataset                      | ML-ready dataset                 |

#### Data Quality Strategy

| Pillar       | What it Means              | Example                    |
| ------------ | -------------------------- | -------------------------- |
| Accuracy     | Data is correct            | Salary is not negative     |
| Completeness | No missing values          | Country field not NULL     |
| Consistency  | Same format across systems | Date format YYYY-MM-DD     |
| Timeliness   | Data is up-to-date         | Real-time transaction data |
| Validity     | Matches defined rules      | Age between 0–120          |
| Uniqueness   | No duplicates              | Unique user ID             |

#### Popular Tools

| Tool            | Type           | Use Case                      | Key Feature               |
| --------------- | -------------- | ----------------------------- | ------------------------- |
| Apache Spark    | Batch + Stream | Big data processing           | Fast, in-memory computing |
| Apache Hadoop   | Batch          | Large-scale storage & compute | HDFS + MapReduce          |
| Apache Kafka    | Streaming      | Real-time pipelines           | High-throughput messaging |
| Apache Flink    | Streaming      | Real-time analytics           | Low latency processing    |
| Apache Airflow  | Orchestration  | Schedule pipelines            | DAG-based workflows       |
| Pandas          | Transformation | Data cleaning & analysis      | Easy Python API           |
| dbt             | Transformation | SQL-based transformations     | Analytics engineering     |
| Talend          | ETL            | Enterprise ETL                | GUI-based pipelines       |
| Snowflake       | Storage        | Analytics                     | Fully managed             |
| Google BigQuery | Storage        | Big data analytics            | Serverless                |

### Model Development and Training

### Model Development and Serving

### Automating Insurance Claim Reviews with MLflow and BentoML

### Data Security and Governance

### Sneak Peek into AWS SageMaker

#### Foundations

##### [Python](https://github.com/jakir-ruet/mastering-with-python)

##### [ML Foundations](https://github.com/jakir-ruet/artificial-intelligence-mastering)

##### Data Science Tools (Numpy, Pandas, Matplotlib)

##### [Git](https://github.com/jakir-ruet/github-actions-master) & [Git Actions](https://github.com/jakir-ruet/github-actions-master)

##### [SQL](https://github.com/jakir-ruet/database-administration-system)

##### [Linux](https://github.com/jakir-ruet/linux-system-administration) with [BASH Scripts](https://github.com/jakir-ruet/bash-scripts-master)

#### Core MLOps Skills

##### [Data Engineering](https://github.com/jakir-ruet/artificial-intelligence-mastering)

##### Feature Engineering

##### Model Training (Tensor Flow, PyTouch)

##### Model Evaluation

#### Frameworks & Libraries

##### ML Flow

##### Kube Flow

##### Apache Flow

##### Tensor Flow Extended (TFX)

##### Data Version Control (DVC)

#### Tooling & Infrastructure

##### Docker

##### Kubernetes

##### CI/CD

##### Cloud Platform (AWS, GCP, Azure)

#### Production & Optimization

##### Model Development

##### Model Monitoring

##### Scaling ML Models

#### Advanced & Specializations

## With Regards, `Jakir`

[![LinkedIn][linkedin-shield-jakir]][linkedin-url-jakir]
[![Facebook-Page][facebook-shield-jakir]][facebook-url-jakir]
[![Youtube][youtube-shield-jakir]][youtube-url-jakir]

### Wishing you a wonderful day! Keep in touch

<!-- Personal profile -->

[linkedin-shield-jakir]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url-jakir]: https://www.linkedin.com/in/jakir-ruet/
[facebook-shield-jakir]: https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white
[facebook-url-jakir]: https://www.facebook.com/jakir.ruet/
[youtube-shield-jakir]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[youtube-url-jakir]: https://www.youtube.com/@mjakaria-ruet/featured
