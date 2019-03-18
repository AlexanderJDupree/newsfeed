'''
File: test_requests.py

Brief: Unit tests for https requests helper for newsfeed app

Author: Alexander DuPree

'''
import unittest
import requests
from helpers.newsAPI import NewsAPI

class TestRequests(unittest.TestCase):

    news_url = "https://newsapi.org/v2/top-headlines?"

    ''' News Api returns apiKeyMissing error code 401 '''
    def testMissingApiKey(self):
        r = requests.get(self.news_url)
        self.assertEqual(r.status_code, 401)

    ''' News Api returns apiKeyInvalid error code 401 '''
    def testInvalidAPIKey(self):
        r = requests.get(self.news_url + "apiKey=APIKEY")
        self.assertEqual(r.status_code, 401)

    def testValidNewsRequest(self):

        query = { 'top': '10', 'country': 'us' }

        response = NewsAPI.request(query)
        self.assertEqual(response['status'], 'ok')

if __name__ == '__main__':
    unittest.main()

