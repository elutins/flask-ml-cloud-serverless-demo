install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

make lint:
	ruff check .

make format:
	black *.py

make test:
	pytest-v test_app_post_request.py

install_conda_env:
	conda env create -f environment/conda_env.yml &&\
	conda activate .flask-ml-cloud-serverless-demo

