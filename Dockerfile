FROM python:3.7-slim

WORKDIR /app

COPY . /app

ARG VER=0.0.1

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python", "newsfeed/newsfeed"]
