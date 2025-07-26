.PHONY: help setup venv install run forecast clean

VENV ?= .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

help:
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "  setup       Create virtual environment and install dependencies"
	@echo "  install     Install dependencies from requirements.txt"
	@echo "  prepare     Run data preparation script (data_preparation.py)"
	@echo "  train       Train model (train.py)"
	@echo "  register    Register model to MLflow (register.py)"
	@echo "  predict     Run inference (inference.py)"
	@echo "  all         Run full pipeline: prepare → train → register → predict"
	@echo "  clean       Remove virtualenv and Python cache files"
	@echo ""

setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install:
	$(PIP) install -r requirements.txt

prepare:
	PYTHONPATH=. $(PYTHON) src/data_preparation.py

train:
	PYTHONPATH=. $(PYTHON) src/models/train.py

register:
	PYTHONPATH=. $(PYTHON) src/models/register.py

predict:
	PYTHONPATH=. $(PYTHON) src/inference.py

evaluate:
	PYTHONPATH=. $(PYTHON) src/models/evaluation.py

all: prepare train register predict

clean:
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

