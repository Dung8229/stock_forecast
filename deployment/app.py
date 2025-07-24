from src.models.inference import inference_flow
from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/prefecthq/demo.git",
        entrypoint="deployment/app.py:inference_flow",
    ).deploy(
        name="test-managed-flow",
        work_pool_name="zoomcamps-pool",
    )