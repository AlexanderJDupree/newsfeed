'''
File: newsApi.py

Brief: newsAPI.py handles https requests to the News API server and returns a 
       json object on successfull requests

Author: Alexander DuPree

'''

import os
import requests
from helpers.urlBuilder import URL

class NewsAPI:

    NEWS_API      = "https://newsapi.org/v2/"
    TOP_HEADLINES = "top-headlines?"
    API_KEY = os.environ['NEWS_API_KEY'] if 'NEWS_API_KEY' in os.environ.keys() else None

    ALIASES = { 'keyword' : 'q', 'top' : 'pageSize' }

    @classmethod
    def __buildURL(cls, query):
        url = URL(cls.NEWS_API, cls.TOP_HEADLINES, query=query, aliases=cls.ALIASES)
        url.append({'apiKey' : cls.API_KEY})
        return url

    @classmethod
    def request(cls, query):
        url = cls.__buildURL(query)

        response = requests.get(url)

        return response.json()

