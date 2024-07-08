[![Simple Azure Flask Web App | Python 3.12](https://github.com/elutins/flask-ml-cloud-serverless-demo/actions/workflows/main.yml/badge.svg)](https://github.com/elutins/flask-ml-cloud-serverless-demo/actions/workflows/main.yml)

## Simple Flask App Hosted by Azure

### Overview

This repo contains source code to deploy a simple Flask web application via Microsoft Azure. The purpose of this repo is to demo building the Flask app, deploying the app inside of Azure cloud, and creating a CI/CD pipeline with `Github Actions`.

The app hosts a simple Random Forest model endpoint for predicting salaries of NHL players. As of _7/2/2024_, the application can be accessed at [https://flask-ml-service-v2.azurewebsites.net/](https://flask-ml-service-v2.azurewebsites.net/). Predictions can be made against the model by sending a `POST` request to the url with the `/predict` endpoint (`https://flask-ml-service-v2.azurewebsites.net/predict`). Alternatively, running `./make_predictions_request_azure_app.sh` from the root of this directory will send a POST request for a sample dataset of 10 players to the app endpoint. The source code of the actual Flask app can be found in [app.py](https://github.com/elutins/flask-ml-cloud-serverless-demo/blob/main/app.py)

**NOTE:** Considering the purpose of this app is geared towards building a CI/CD pipeline with GitHub Actions, creating a good performing model was not a focal point. In fact, it is a poor performing model from a metric standpoint, intentionally. 

### Makefile Targets

The `Makefile` includes five targets in total. Note, it is recommended to create a virtual environment prior to running `make install`. If you want to create a conda environment instead of a traditional venv environment, commands to do so are run via `make install_conda_env` target (described later below):

1. `install`: install all libraries set in `requirements.txt` using pip
2. `lint`: runs ruff against all python files in repo for linting purposes
3. `format`: runs black against all python files in repo for formatting purposes
4. `test`: test that the app endpoint returns a `200` response code
5. `install_conda_env`: installs all packages set in conda_env.yml inside a conda environment (assumes that a conda environment named `.flask-ml-cloud-serverless-demo` has already been created) and activates that environment. The purpose being that, if running locally, users can run the Flask app using the `conda` environment if desired instead of a traditional `pypi` environment. 


### GitHub Actions Build Commands

On pushing a new commit to the main branch, GitHub Actions has been setup to run three commands from the `Makefile`:

```
make install
make lint
make test
```

The GitHub Actions workflow can be seen in [.github/workflows/main.yml](https://github.com/elutins/flask-ml-cloud-serverless-demo/blob/main/.github/workflows/main.yml). 



### Running model predictions against app endpoint.

Running `./make_predictions_request_azure_app.sh` from the root of this directory will send a `POST` request for a sample dataset of 10 players to the app endpoint. One record of the sample data (as a python dictionary) looks like such:
```
sample_record = {
    "plusMinus": {
        "0": -4,
    },
    "Position": {
        "0": "D",
    },
    "G": {
        "0": 0,
    },
    "A1": {
        "0": 1,
    },
    "GP": {
        "0": 36,
    },
    "Grit": {
        "0": 139,
    },
    "TOI%": {
        "0": 23.8,
    },
    "xGA": {
        "0": 24.3,
    },
    "xGF": {
        "0": 16.7,
    },
    "First Name": {
        "0": "Alex",
    },
    "Last Name": {
        "0": "Biega",
    },
    "Team": {
        "0": "VAN",
    }
```
