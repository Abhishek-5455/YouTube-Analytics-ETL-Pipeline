# YouTube-Analytics-ETL-Pipeline

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline for YouTube analytics data using Apache Airflow. It extracts data from the YouTube Data API, transforms it, and loads it into a PostgreSQL database. The data can then be visualized using Power BI for comprehensive analytics insights.

## Tech Stack
- 🐍 **Python**: Programming language for data processing and pipeline logic
- 🔄 **Apache Airflow**: Workflow orchestration and scheduling
- 🗄️ **PostgreSQL**: Database for storing analytics data
- 🐳 **Docker**: Containerization for easy deployment
- 📺 **YouTube Data API**: Source of YouTube analytics data
- 📊 **Power BI**: Business intelligence and data visualization

## Prerequisites
- Docker Desktop installed and running
- Power BI Desktop (for local visualization) or Power BI Online account
- YouTube Data API key from Google Cloud Console

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

## Connecting PostgreSQL Database to Power BI

### Step 1: Enable PostgreSQL Remote Connections
Ensure PostgreSQL is accessible. Update your `docker-compose.yml` to expose the PostgreSQL port:
```yaml
postgres:
  ports:
    - "5432:5432"
```

### Step 2: Install Power BI PostgreSQL Driver
- Download and install the PostgreSQL ODBC driver from [here](https://www.postgresql.org/download/windows/)
- On Windows: Use the PostgreSQL ODBC driver installer
- On macOS/Linux: Install via package manager

### Step 3: Connect Power BI to PostgreSQL Database

**Using Power BI Desktop:**
1. Open Power BI Desktop
2. Click **Get Data** → **More...**
3. Search for and select **PostgreSQL database**
4. Enter the connection details:
   - **Server**: `localhost` (or your server IP)
   - **Database**: `airflow` (or your database name)
   - **Port**: `5432` (default)
5. Click **OK**
6. Select **Database** authentication mode
7. Enter credentials:
   - **Username**: `airflow`
   - **Password**: (from your docker-compose configuration)
8. Click **Connect**

**Using Power BI Online:**
1. Install and configure **On-premises Data Gateway**
2. Open Power BI Service → **Get Data**
3. Select **PostgreSQL database**
4. Enter your PostgreSQL connection details
5. Configure the gateway connection
6. Click **Connect**

### Step 4: Load Tables
- After connecting, select the tables you want to analyze (e.g., `youtube_data`, `channel_stats`)
- Click **Load** to import data into Power BI

### Step 5: Create Reports and Dashboards
- Use Power BI's visualization tools to create charts, graphs, and dashboards
- Create metrics for:
  - Video performance analysis
  - Channel growth trends
  - Engagement metrics
  - Audience demographics

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