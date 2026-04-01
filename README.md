# YouTube-Analytics-ETL-Pipeline

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for YouTube analytics data using Apache Airflow. It extracts data from the YouTube Data API, transforms it, and loads it into a PostgreSQL database for analysis.

## Tech Stack
- **Python**: Programming language for data processing and pipeline logic
- **Apache Airflow**: Workflow orchestration and scheduling
- **PostgreSQL**: Database for storing analytics data
- **Docker**: Containerization for easy deployment
- **YouTube Data API**: Source of YouTube analytics data

## Prerequisites
- Docker Desktop installed and running

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Abhishek-5455/YouTube-Analytics-ETL-Pipeline.git
cd YouTube-Analytics-ETL-Pipeline
```

### 2. Create Logs Directory
```bash
mkdir logs
```

### 3. Create Environment File
Create a `.env` file in the root directory and add your YouTube API key:
```bash
echo "YOUTUBE_API_KEY=your_youtube_api_key_here" > .env
```

**Note**: Replace `your_youtube_api_key_here` with your actual YouTube Data API v3 key. You can obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).

### 4. Run Docker Compose
```bash
docker-compose up -d
```

This command will:
- Start PostgreSQL database
- Initialize Airflow database
- Create an admin user (username: admin, password: admin)
- Start the Airflow webserver

### 5. Access Airflow Web UI
Once the containers are running, access the Airflow web interface at:
- **URL**: http://localhost:8080
- **Username**: admin
- **Password**: admin

## Usage
- Navigate to the Airflow web UI
- Enable the `youtube_pipeline` DAG
- Trigger the DAG manually or wait for the scheduled run

## Project Structure
- `dags/`: Contains Airflow DAGs and task definitions
- `logs/`: Airflow execution logs
- `plugins/`: Custom Airflow plugins
- `config/`: Configuration files
- `docker-compose.yml`: Docker Compose configuration

## Stopping the Pipeline
To stop the running containers:
```bash
docker-compose down
```