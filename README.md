PYTHONPATH=. python src/data_preparation.py
PYTHONPATH=. python src/models/train.py
PYTHONPATH=. python src/models/register.py
PYTHONPATH=. python src/inference.py

prefect work-pool create zoomcamps-pool --type prefect:managed