'''
File: test_requests.py

Brief: Unit tests for https requests helper for newsfeed app

Author: Alexander DuPree

'''
import unittest
import requests
from helpers.newsAPI import NewsAPI

class TestNewsAPI(unittest.TestCase):

    news_url = "https://newsapi.org/v2/top-headlines?"

    keys = ['top', 'country', 'keyword', 'category', 'sources']

    ''' Test default API request from Newsfeed app '''
    def testValidNewsRequest(self):

        query = { 'top': '10', 'country': 'us' }

        response = NewsAPI.request(query)
        self.assertEqual(response['status'], 'ok')
        return

    ''' News API sources flag cannot be mixed with category or keyword'''
    def testSourcesFlag(self):
        query = dict(zip(self.keys, ['10', 'us', 'harambe', 'general', 'cnn']))

        response = NewsAPI.request(query)
        self.assertEqual(response['code'], 'parametersIncompatible')
        return

    def testInvalidQueriesReturnOK(self):

        query = dict(zip(self.keys, ['10', 'zzsdf', 'asdfasdf', 'gegegeg']))

        response = NewsAPI.request(query)

        self.assertEqual(response['status'], 'ok')
        return

if __name__ == '__main__':
    unittest.main()

