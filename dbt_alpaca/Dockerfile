From python:3.10-slim

WORKDIR /opt/dagster/app/

COPY requirements.txt .

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt


# Default entrypoint so we can run commands like:
# docker-compose run dbt run ...
ENTRYPOINT ["dbt"]