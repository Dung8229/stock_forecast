PYTHONPATH=. python src/data_preparation.py
PYTHONPATH=. python src/models/train.py
PYTHONPATH=. python src/models/register.py
PYTHONPATH=. python src/inference.py

# Gold Price Forecasting - Final Project (MLOps Zoomcamp)

Welcome to the final project of the **MLOps Zoomcamp** – a complete end-to-end MLOps pipeline to forecast the next day's gold price. This repository implements modern MLOps practices using Prefect, MLflow, AWS, and more.

> 🔗 **Project repository:** [github.com/Dung8229/stock\_forecast](https://github.com/Dung8229/stock_forecast/tree/master)

---

## 📌 Project Overview

This project forecasts the **next day's closing price** of gold using a simple machine learning model with **Exponential Moving Average (EMA)** as a feature. The emphasis is on building a robust and automated MLOps pipeline.

---

## 🔧 Key Components

### ✅ MLflow for Experiment Tracking

* Tracks experiments, parameters, and metrics.
* Registers the best model automatically into the MLflow Model Registry.

### ✅ Prefect for Workflow Orchestration

* Modularized tasks (data loading, feature engineering, training, evaluating, registering).
* Prefect Cloud used for deployment.
* Scheduled to run daily.
* Flow stores:

  * Data & model artifacts → **Amazon S3**
  * Run metadata → **PostgreSQL (Neon remote)**

### ✅ Monitoring with Grafana

* RMSE is monitored via Grafana dashboard.
* Automatic alerts sent (e.g., when RMSE drops below a threshold).

### ✅ Testing

* Unit tests implemented with **pytest**.
* Includes tests for data processing, model logic, and pipeline integrity.

### ✅ Makefile for Automation

* Common commands scripted for easy development and CI/CD tasks:

  * `make train`
  * `make test`
  * `make deploy-flow`

---

## 📦 Folder Structure (planned)

```
stock_forecast/
├── data/               # Sample & test data
├── notebooks/          # Experimentation & EDA
├── src/
│   ├── features/       # Feature engineering scripts
│   ├── models/         # Training, prediction, evaluation
│   ├── pipeline/       # Prefect tasks and flows
├── tests/              # Pytest test cases
├── Makefile
├── prefect.yaml        # Deployment spec
├── requirements.txt
├── README.md
```

---

## 🚀 Features Planned

* [x] Daily auto-prediction via Prefect Cloud
* [x] MLflow model registry integration
* [x] Store artifacts on S3
* [x] Track runs on Neon (PostgreSQL)
* [x] Send alerts via Grafana
* [x] CI-style test with pytest
* [ ] Docker containerization for full reproducibility
* [ ] Kubernetes deployment (optional stretch goal)

---

## 🧠 Tech Stack

* **MLflow**
* **Prefect 2.0 (Cloud)**
* **Amazon S3**
* **Neon PostgreSQL**
* **Grafana**
* **pytest**
* **Makefile**
* *(Possible upcoming: Docker, Kubernetes)*

---

## 📅 Flow Schedule & Automation

* Trigger: Daily @ 6PM
* Action: Predict gold closing price for the next trading day.
* Storage: Prefect stores data in S3, and metadata in Neon.
* Monitoring: Grafana watches the metrics, sends alerts.

---

## 📬 Contact

For questions or feedback, please open an issue or reach out via GitHub.

---

> 🚧 **Note**: This project is still in development. Some components (e.g., Docker, K8s) are under construction.
