# FROM bde2020/spark-python-template:2.4.5-hadoop2.7
FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt install -y libpq-dev gcc
RUN pip install numpy scipy pandas matplotlib
RUN pip install psycopg2

COPY . /app

CMD sleep 86400
