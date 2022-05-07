# SW_ETL

## run locally

- [install docker](https://docs.docker.com/engine/install/)
- [install docker-compose](https://docs.docker.com/compose/install/)

for the first time
```bash
docker-compose up --build
```

next run this
```bash
docker-compose up
```

## tests

```bash
docker-compose run sw_etl pytest
```

## contributing

If you want to introduce some changes to this project you need to set up an environment locally. Best way to do this
is to use python virtual environment (I am using `pyenv`). The easiest way (without `pyenv`) is to use bare python
virtualenv (please remember that we are using python3.10 in this project).

```bash
python -m venv venv
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

next you need to install `pre-commit` hooks (set of scripts that are making sure that your code is clean and ready
to be pushed to github).

```bash
pre-commit install
```

### adding requirements

If you want to add new libraries to this project you need to add them to `requirements.in` file (for general
requirements) or to `requirements-dev.in` (for development use). Next, please compile the requirements.

```bash
pip-compile requirements.in
pip-compile requirements-dev.in
```
