### Airflow Install

- [Docker Composer](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- Make Environment

Create `.env` and UID

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Generate `FERNET_KEY` and put on `.env`

```bash
openssl rand -base64 32
FERNET_KEY=your_generated_key
```

Put these on `.env`, if needed

```bash
AIRFLOW_IMAGE_NAME=apache/airflow:2.9.3
```

```bash
mkdir -p ./dags ./logs ./plugins ./data
docker compose up airflow-init
docker compose up
```

Access UI

```bash
http://localhost:8080 # user: airflow & password: airflow)
```
