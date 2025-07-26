# Stock Forecasting Project

## 🚀 Problem Description

In financial markets, predicting stock price trends is a valuable yet challenging task due to high volatility and noise. This project aims to build an end-to-end machine learning pipeline to forecast stock prices using historical data. The goal is to automate the forecasting process, from data ingestion to model training, registration, deployment, and monitoring, following modern MLOps practices. The project focuses on simplicity in modeling (using Exponential Moving Average) to highlight the MLOps lifecycle rather than complex model performance.

---

## ☁️ Cloud Infrastructure

* The project uses S3 bucket to store both data and model artifacts.
* MLflow backend is hosted on Neon.tech (a remote PostgreSQL database).
* Prefect deployments and flows are configured to run daily in the cloud.

---

## 🎯 Experiment Tracking and Model Registry

* **MLflow** is used for:

  * **Tracking experiments**: Log RMSE metrics, parameters, and versions.
  * **Model registry**: The best-performing model can be registered and versioned.

* MLflow uses Neon.tech as the remote backend.

---

## 🔁 Workflow Orchestration

* **Prefect 2.0** is used as the orchestration tool.
* The flow includes the following tasks:

  * Data preparation
  * Model training
  * Model registration
  * Daily inference
  * Model evaluation (for monitoring)

* The inference flow is deployed via `prefect.yaml`

---

## 📦 Model Deployment

* The trained model is registered with MLflow, but not deployed as a container or REST API.
* Instead, model inference is performed by a Prefect deployment, scheduled to run daily.
* This automated flow pulls the latest model from the MLflow registry and generates forecasts for the upcoming day.
* All secrets and environment variables (e.g., AWS credentials) are managed through Prefect job variables

---

## 📈 Model Monitoring

* RMSE on test data is computed and pushed to Prometheus Pushgateway.
* Grafana dashboards are set up to visualize metrics, hosted via Docker Compose.
* To start the monitoring system:
```bash
cd monitor
docker compose up
```
* Then send the latest RMSE to Prometheus using:
```bash
make evaluate
```
* Monitoring logic checks if RMSE exceeds a threshold → send an alert to dashboard.

---

## 📦 Reproducibility

* The entire pipeline can be reproduced using:

  * A clear `Makefile`
  * `requirements.txt`
  * Python scripts organized in a `src/` directory

---

## ✅ Best Practices

* ✅ **Unit tests**: Some key functions are covered with `pytest`
* ✅ **Makefile**: Automates common tasks like training, inference, cleaning
* ✅ **Linter**: `flake8` with `black` used for formatting
* ⚠️ **Pre-commit hooks**: Not yet implemented
* ⚠️ **Integration test**: Not yet implemented
* ⚠️ **CI/CD pipeline**: Not yet implemented

---

## 🛠 Project Structure

```
stock_forecast/
├── data/                        # input and output datasets
├── src/
│   ├── data_preparation.py     # prepare features with EMA
│   ├── models/
│   │   ├── train.py            # train model
│   │   └── register.py         # register model to MLflow
│   └── inference.py            # run predictions
├── prefect/                    # orchestration flows
├── Dockerfile                  # model deployment container
├── Makefile                    # workflow automation
├── requirements.txt            # dependencies
├── tests/                      # unit tests
└── README.md                   # you are here
```

---

## 🔄 Makefile Usage

```bash
make help           # Show available commands
make setup          # Create virtualenv and install requirements
make prepare        # Run data preparation
make train          # Train the model
make register       # Register model to MLflow
make predict        # Run inference
make all            # Run full pipeline
make clean          # Delete cache and virtualenv
```

---

## 🧪 Run Locally

```bash
# Clone the repository
$ git clone https://github.com/Dung8229/stock_forecast.git
$ cd stock_forecast

# Create environment & install dependencies
$ make setup

# Run full pipeline
$ make all

# Run inference
$ make predict
```