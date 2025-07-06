# 

FROM python:3.13-slim

WORKDIR /opt/dagster/app/

COPY requirements.txt .

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt


COPY . .

CMD ["tail", "-f", "/dev/null"]
