# FastAPI-Postgres Homelab Template

Template for running FastAPI Microservice with a Postgres Database w/ Monitoring on a home server

## Tools

- FastAPI
- Postgres
- Prometheus
- Grafana
- Docker

## References

|    Developer    |                                             Repository                                             |
| :-------------: | :------------------------------------------------------------------------------------------------: |
|    Tiangolo     |                           [FastAPI](https://github.com/tiangolo/fastapi)                           |
|    Trallnag     | [prometheus-fastapi-instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator) |
|     Kludex      |         [fastapi-prometheus-grafana](https://github.com/Kludex/fastapi-prometheus-grafana)         |
| Code-Specialist |              [fastapi-keycloak](https://github.com/code-specialist/fastapi-keycloak)               |

### Articles

Josh Campos: [FastAPI API Key](https://itsjoshcampos.codes/fast-api-api-key-authorization)

# Getting Started

## <img src="https://python-poetry.org/images/logo-origami.svg" alt="My logo" width="16" height="16"> Poetry Package Manager

Poetry is a python package management tool that creates a better development for the python ecosystem. If you are not familiar with the package you can refer to the [documentation](https://python-poetry.org/docs/).

```
$ pip install poetry
$ poetry install
```

### Run containers

```
$ docker-compose up -d
```

- View Grafana Dashboards at localhost:3000

  - default creds:
    - user: admin
    - pwd: fastapi

- FastAPI endpoints at localhost:8000
