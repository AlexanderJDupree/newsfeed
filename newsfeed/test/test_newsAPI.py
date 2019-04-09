'''
File: test_newsAPI.py

Brief: Unit tests for https requests helper for newsfeed app

Author: Alexander DuPree

'''
import unittest
from helpers.newsAPI import NewsAPI

class TestNewsAPI(unittest.TestCase):

    news_url = "https://newsapi.org/v2/top-headlines?"

    keys = ['top', 'country', 'keyword', 'category', 'sources']

    def testValidNewsRequest(self):

        query = { 'top': '10', 'country': 'us' }

        response = NewsAPI.request(query)
        self.assertEqual(response['status'], 'ok')
        return

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

