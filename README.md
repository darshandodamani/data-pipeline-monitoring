# Data Pipeline Monitoring with Apache Airflow

A complete ETL (Extract, Transform, Load) data pipeline built with Apache Airflow, Docker, and Python. This project demonstrates automated data processing from CSV files to a SQLite database with monitoring and scheduling capabilities.

## 🚀 Features

- **Automated ETL Pipeline**: Extract data from CSV, transform it, and load into SQLite database
- **Apache Airflow Integration**: Full workflow orchestration and monitoring
- **Docker Containerization**: Easy deployment and environment consistency
- **Data Validation**: Automatic data cleaning and filtering
- **Web-based Monitoring**: Airflow UI for pipeline visualization and management

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.10+ (for local development)
- Git

## 🏗️ Project Structure

```
data-pipeline-monitoring/
├── dags/                          # Airflow DAG definitions
│   └── etl_dag.py                 # Main ETL pipeline DAG
├── etl/                           # ETL modules
│   ├── extract.py                 # Data extraction logic
│   ├── transform.py               # Data transformation logic
│   └── load.py                    # Data loading logic
├── docker/                        # Docker configuration
│   └── docker-compose.yml         # Multi-container setup
├── logs/                          # Airflow logs (auto-generated)
├── plugins/                       # Airflow plugins (auto-generated)
├── mock_transactions.csv          # Sample data file
├── pipeline.db                    # SQLite output database
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd data-pipeline-monitoring
```

### 2. Create Required Directories

```bash
mkdir -p logs plugins
sudo chown -R 50000:0 .
sudo chmod -R 775 .
```

### 3. Start the Services

```bash
cd docker
docker compose down -v  # Clean any existing setup
docker compose up airflow-init  # Initialize Airflow
docker compose up -d  # Start all services
```

### 4. Access Airflow Web UI

- **URL**: http://localhost:8080
- **Username**: `admin`
- **Password**: `admin`

## 📊 Pipeline Overview

### ETL Process

1. **Extract** (`extract.py`):

   - Reads transaction data from `mock_transactions.csv`
   - Validates file existence and format
   - Returns pandas DataFrame

2. **Transform** (`transform.py`):

   - Removes rows with null values
   - Filters for completed transactions only
   - Data quality validation

3. **Load** (`load.py`):
   - Writes cleaned data to SQLite database
   - Creates/replaces `transactions` table
   - Handles database connections and errors

### Sample Data Format

```csv
transaction_id,amount,status,date
1,100.50,Completed,2024-01-01
2,250.00,Pending,2024-01-02
3,75.25,Completed,2024-01-03
```

## 🐳 Docker Services

| Service        | Description               | Port |
| -------------- | ------------------------- | ---- |
| `postgres`     | Airflow metadata database | 5432 |
| `airflow-init` | One-time initialization   | -    |
| `webserver`    | Airflow web interface     | 8080 |
| `scheduler`    | Airflow task scheduler    | -    |

## 📝 Usage

### Running the Pipeline

1. **Access Airflow UI**: Navigate to http://localhost:8080
2. **Enable DAG**: Toggle the `etl_pipeline` DAG to "On"
3. **Trigger Run**: Click the "Trigger DAG" button
4. **Monitor Progress**: Watch task execution in real-time

### Viewing Results

```bash
# Check the generated database
sqlite3 pipeline.db
sqlite> SELECT * FROM transactions WHERE status = 'Completed';
sqlite> .exit
```

### Checking Logs

```bash
# View service logs
docker compose logs webserver
docker compose logs scheduler

# Follow logs in real-time
docker compose logs -f
```

## 🔧 Configuration

### Environment Variables

Key Airflow configurations in `docker-compose.yml`:

```yaml
AIRFLOW__CORE__EXECUTOR: LocalExecutor
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__CORE__LOAD_EXAMPLES: "false"
_PIP_ADDITIONAL_REQUIREMENTS: "pandas sqlalchemy python-dotenv"
```

### Customizing the Pipeline

1. **Modify Data Source**: Update `CSV_PATH` in `dags/etl_dag.py`
2. **Change Schedule**: Modify `schedule_interval` parameter
3. **Add Transformations**: Extend logic in `etl/transform.py`
4. **Different Output**: Modify database connection in `etl/load.py`

## 📈 Monitoring & Troubleshooting

### Common Issues

1. **Permission Denied Errors**:

   ```bash
   sudo chown -R 50000:0 /path/to/project
   sudo chmod -R 775 logs plugins
   ```

2. **Services Not Starting**:

   ```bash
   docker compose down -v
   docker compose up airflow-init
   docker compose up -d
   ```

3. **DAG Not Appearing**:
   - Check file is in `dags/` directory
   - Verify Python syntax
   - Check Airflow logs for import errors

### Health Checks

```bash
# Check service status
docker compose ps

# Test database connection
docker compose exec webserver airflow db check

# Validate DAG syntax
docker compose exec webserver airflow dags list
```

## 🚀 Development

### Local Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run ETL components individually
cd etl
python extract.py
python transform.py
python load.py
```

### Adding New Features

1. **New DAG**: Create Python file in `dags/` directory
2. **Custom Operators**: Add to `plugins/` directory
3. **Dependencies**: Update `requirements.txt` and `_PIP_ADDITIONAL_REQUIREMENTS`

## 📚 Dependencies

- **Apache Airflow 2.7.3**: Workflow orchestration
- **PostgreSQL 15**: Metadata database
- **Python 3.10**: Runtime environment
- **Pandas**: Data manipulation
- **SQLAlchemy**: Database ORM
- **Python-dotenv**: Environment management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [Troubleshooting](#monitoring--troubleshooting) section
2. Review Docker and Airflow logs
3. Open an issue on GitHub

## 🙏 Acknowledgments

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Docker Official Documentation](https://docs.docker.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

**Happy Data Processing!** 🎉
