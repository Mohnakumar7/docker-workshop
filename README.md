# docker-workshop
Workshop Codespaces

This README file is designed for a GitHub repository based on the first module of the **Data Engineering Zoomcamp**, specifically focusing on the updated session covering **Docker, Postgres, and real-world workflows**.

***

# Data Engineering Zoomcamp: Module 1 - Docker & Postgres

This repository contains the updated content for Module 1 of the Data Engineering Zoomcamp. The primary focus of this workshop is to introduce **Docker** and **Postgres** within a data engineering context, specifically by building a pipeline that ingests New York taxi data into a database.

## 🚀 Overview
The project demonstrates how to:
* Set up a **remote development environment** using GitHub Codespaces.
* Use **`uv`**, a fast Python package manager written in Rust, for dependency and virtual environment management.
* **Dockerize** a Python data pipeline to ensure reproducibility.
* Orchestrate multiple services (Postgres and PGAdmin) using **Docker Compose**.
* Ingest large CSV datasets into a Postgres database using **Pandas** and **SQL Alchemy**.

## 🛠 Prerequisites:
* A **GitHub account** (to use Codespaces).
* **Docker** installed (pre-installed in Codespaces).
* **Python** (pre-installed in Codespaces).
* **Visual Studio Code Desktop** is recommended for a better development experience compared to the browser.

## 📁 Project Structure
* `pipeline.py`: A simple parameterized script to demonstrate Python in Docker.
* `ingest_data.py`: The main ingestion script that downloads CSV data and uploads it to Postgres.
* `Dockerfile`: Instructions for building the dockerized ingestion image.
* `docker-compose.yaml`: Configuration for running Postgres and PGAdmin together.
* `pyproject.toml` / `uv.lock`: Dependency management files created by `uv`.

## ⚙️ Setup Instructions

### 1. Environment Setup
1. Create a new repository and launch it in a Codespace.
2. Configure your terminal prompt (optional) to make it more readable.

### 2. Dependency Management with `uv`
This project uses **`uv`** for managing the virtual environment because it is significantly faster than traditional tools.
* **Initialize `uv`**: `uv init --python 3.13`.
* **Add dependencies**: `uv add pandas sqlalchemy psychopg2-binary`.
* **Run scripts**: `uv run python ingest_data.py [params]`.

### 3. Running Postgres and PGAdmin
Use **Docker Compose** to start the database and the web-based management interface.
```bash
docker-compose up
```
* **Postgres**: Accessible on port `5432`.
* **PGAdmin**: Accessible on port `8085`.

### 4. Dockerizing the Ingestion Pipeline
To build and run the ingestion script as a standalone container:
1. **Build the image**: `docker build -t taxi_ingest .`.
2. **Run the container** (ensuring it is on the same network as the database):
```bash
docker run -it --network=pg-network taxi_ingest \
  --user=root --password=root --host=pg-database --port=5432 \
  --db=ny_taxi --table_name=yellow_taxi_data \
  --url=[CSV_URL]
```
*(Note: Use the container name `pg-database` instead of `localhost` when running inside a Docker network)*.

## 📊 Data Pipeline Details
The pipeline processes the **New York Taxi dataset**. Because CSV files are "schemaless," the script explicitly defines data types (e.g., converting pickup/drop-off times to datetime objects) to ensure database integrity. Data is loaded in **chunks of 100,000 rows** to manage memory usage efficiently.

## 🔗 Resources
* **Course Link**: [DataTalks.Club Data Engineering Zoomcamp](https://datatalks.club).
* **GitHub Codespaces**: Remote environment used for this workshop.

***
