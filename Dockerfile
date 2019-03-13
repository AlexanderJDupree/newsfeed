FROM python:3.7-slim

MAINTAINER AlexanderJDupree "https://github.com/AlexanderJDupree"

COPY . /app

WORKDIR /app/newsfeed/

ARG VER=0.0.1

RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

ENTRYPOINT ["python"]
CMD ["newsfeed"]

