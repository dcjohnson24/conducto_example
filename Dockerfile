FROM python:3.7-slim
RUN apt update -y && apt install -y unzip libpq-dev build-essential

COPY requirements.txt requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code
WORKDIR /code
