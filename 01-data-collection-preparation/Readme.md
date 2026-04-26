## Data Collection, Clearing and Transformation

These are crucial foundational stages in MLOps, because the quality of a machine learning system depends heavily on the quality of its data pipeline. In real-world ML systems, models are only as good as the data they are trained on. Below is a clear explanation of each stage.

### Data Collection

Data collection is the process of gathering raw data from different sources to build a dataset for machine learning.

#### Common Data Sources

- Databases (MySQL, PostgreSQL, MongoDB)
- APIs (REST / GraphQL services)
- Files (CSV, JSON, Excel, Parquet)
- Logs (application logs, system logs)
- Streaming systems (Kafka, IoT devices)
- Cloud storage (AWS S3, Google Cloud Storage)

#### Key Characteristics in MLOps

- Data is continuously generated and collected
- Stored in a raw and immutable format
- Often automated using pipelines (Airflow, Kafka, ETL jobs)

> **Important Principle**
> Always preserve raw data separately before any processing, so it can be reused or audited later.

### Data Cleaning

Data cleaning is the process of improving data quality by fixing errors, inconsistencies, and missing values.

#### Common Data Issues

- Missing values (NaN/nulls)
- Duplicate records
- Incorrect data types
- Inconsistent formats (dates, strings)
- Outliers and noisy data
- Corrupted or nested fields (e.g., JSON strings)

#### Typical Cleaning Operations

- Handling missing values (mean, median, mode, or removal)
- Removing duplicates
- Fixing data types (string → datetime, float → int)
- Parsing structured data (e.g., JSON fields)
- Detecting and handling outliers

#### MLOps Perspective

- Cleaning rules should be automated and repeatable
- Data validation should be enforced before training
- Pipeline should fail if data quality is poor

### Data Transformation

Data transformation is the process of converting cleaned data into a format that machine learning models can understand.

> **Why it is needed**
> Machine learning models **only work** with **numerical data**, not **raw text** or **inconsistent formats**.

#### Common Transformation Steps

- Feature Engineering
  - Creating new meaningful features from existing data
  - Example: extracting **hire_year** from **hire_date**
- Encoding Categorical Data
  - Converting text into numbers
  - Example: `One-Hot Encoding` for departments ["HR", "IT", "Finance", "Marketing"]

**One-Hot Encoding Means**

| dept_HR | dept_IT | dept_Finance | dept_Marketing |
| ------- | ------- | ------------ | -------------- |
| 1       | 0       | 0            | 0              |
| 0       | 1       | 0            | 0              |
| 0       | 0       | 1            | 0              |

> Machine Learning models cannot understand text directly

- Feature Scaling
  - Standardizing numerical values
  - Example: StandardScaler for age, salary, bonus
- Feature Selection
  - Removing irrelevant or redundant columns (e.g., ID, name, email)

> Example Outcome > After transformation:
>
> - Raw dataset → structured feature matrix
> - Shape becomes something like:
> - (20000 rows, 8 features)
