FROM python:latest

WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install -y \
    python-pip python-dev build-essential && \
    pip install -r requirements.txt && \
    bash nohup run.sh
