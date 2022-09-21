## Poetry initial setup
- Configure Poetry:

```shell
poetry config virtualenvs.in-project false
poetry config virtualenvs.path <conda-install-path>/envs
```

## Packages installation
- Create and activate *conda* virtual environment for development:

```shell
conda create -n venv python=3.10
conda activate venv
```

- Install dependencies with Poetry:

```shell
poetry install
```
## Start project
- Run uvicorn with instance of app:

```shell
uvicorn app.main:app 
```