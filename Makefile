help:
	@cat $(MAKEFILE_LIST)

.PHONY: install
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

.PHONY: lint
make lint:
	ruff check .

.PHONY: format
make format:
	black *.py

.PHONY: test
make test:
	pytest -v test_app_post_request.py

.PHONY: install_conda_env
install_conda_env:
	conda env create -f environment/conda_env.yml &&\
	conda activate .flask-ml-cloud-serverless-demo


