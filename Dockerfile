FROM python:3.7-slim

MAINTAINER AlexanderJDupree "https://github.com/AlexanderJDupree"

COPY . /app

WORKDIR /app/newsfeed/

ARG news_api_key
ENV NEWS_API_KEY=$news_api_key

RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

ENTRYPOINT ["python"]
CMD ["newsfeed.py"]

