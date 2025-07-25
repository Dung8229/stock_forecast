from mlflow.tracking import MlflowClient
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict
from prefect import flow, task
from prefect.assets import materialize
from prefect.artifacts import create_table_artifact, create_markdown_artifact
from src.data_preparation import process_data, data_preparation_flow
from src.models.train import load_data
from src.inference import load_model_from_registry, run_batch_prediction
from sklearn.metrics import root_mean_squared_error
from src.utils.logger import get_logger
logger = get_logger(__name__)
from src.utils.s3_io import upload_df_to_s3, download_df_from_s3, download_joblib_from_s3
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random

@flow(name="Evaluate Current Model")
def evaluate_model_flow():
    data_preparation_flow()
    _, df_tst = load_data()
    model = load_model_from_registry()
    y_pred = run_batch_prediction(model=model, df_infer=df_tst, for_evaluate=True)['Prediction']
    y_true = df_tst['Next_Close']
    rmse_value = root_mean_squared_error(y_true, y_pred)
  
    # Pushgateway
    registry = CollectorRegistry()
    rmse_metric = Gauge("stock_forecast_test_rmse", "RMSE on test data", registry=registry)
    rmse_metric.set(rmse_value)

    # Push lên Pushgateway
    push_to_gateway('localhost:9091', job='stock_forecast_evaluator', registry=registry)

    logger.info(f"Pushed RMSE {rmse_value} to Pushgateway")
    return rmse_value

def alert_triggered():
    rmse_value = random.randint(21, 30)
  
    # Pushgateway
    registry = CollectorRegistry()
    rmse_metric = Gauge("stock_forecast_test_rmse", "RMSE on test data", registry=registry)
    rmse_metric.set(rmse_value)

    # Push lên Pushgateway
    push_to_gateway('localhost:9091', job='stock_forecast_evaluator', registry=registry)

    logger.info(f"Pushed RMSE {rmse_value} to Pushgateway")
    return rmse_value

if __name__ == "__main__":
    # evaluate_model_flow()
    alert_triggered()
  