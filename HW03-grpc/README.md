## Poetry initial setup
- Configure Poetry:

```shell
poetry config virtualenvs.in-project false
poetry config virtualenvs.path <conda-install-path>/envs
```

## Packages installation
- Create and activate *conda* virtual environment for development:

```shell
conda create -n grpcTest python=3.10
conda activate grpcTest
```

- Install dependencies with Poetry:

```shell
poetry install
```

## Start project
- Compile proto file:

```shell
python -m grpc_tools.protoc -I definitions/ --python_out=definitions/builds/ --grpc_python_out=definitions/builds/ definitions/service.proto
```

- Run server:

```shell
python3 -m app
```

- Run client:

```shell
python3 -m app.client
```

## Run tests
- Run tests:

```shell
pytest

```
