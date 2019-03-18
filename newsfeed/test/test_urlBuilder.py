'''
File: test_urlencoder.py

Brief: Unit tests for newsfeed urlencoder helper

Author: Alexander DuPree

'''
import unittest

from helpers.urlBuilder import URL

class TestURLString(unittest.TestCase):

    origin = "https://newsapi.org/v2/"
    headline_endpoint = "top-headlines?"

    aliases = { 'keyword' : 'q', 'top' : 'pageSize' }

    keys = ['country', 'keyword', 'category', 'apiKey', 'sources']

    required = ['apiKey']


    ''' URL requires origin, endpoint, and anything specified in required '''
    def testRequiredSegments(self):
        query = {'missing': 'required', 'segments' : 'fails'}
        url = URL(self.origin, self.headline_endpoint, required=['apiKey'])
        self.assertRaises(Exception, url.encode, query)


    ''' Sample valid News API query '''
    def testTopHeadlineRequest(self):

        payload = ['us', 'harambe', 'business', 'API_KEY']

        query = dict(zip(self.keys, payload))

        expectedURL = (
                'https://newsapi.org/v2/top-headlines?'
                'country=us&'
                'category=business&'
                'apiKey=API_KEY&'
                'q=harambe'
                )

        url = URL(self.origin, self.headline_endpoint, query=query, aliases=self.aliases)
        self.assertEqual(url, expectedURL)
        return

    ''' Default query from newsfeed app, contains None values. '''
    def testURLStripsNoneValues(self):
        query = { 'top': '10', 'country': 'us', 'keyword': None, 
                'category': None, 'sources': None, 'apiKey': 'API_KEY' }

        expectedURL = (
                'https://newsapi.org/v2/top-headlines?'
                'country=us&'
                'apiKey=API_KEY&'
                'pageSize=10'
                )

        url = URL(self.origin, self.headline_endpoint, query=query, aliases=self.aliases)
        self.assertEqual(url.url, expectedURL)

    ''' Appending query segments to constructed URL '''
    def testURLAppend(self):
        payload = ['us', 'harambe', 'business']

        query = dict(zip(self.keys, payload))

        expectedURL = (
                'https://newsapi.org/v2/top-headlines?'
                'country=us&'
                'category=business&'
                'q=harambe&'
                'apiKey=API_KEY'
                )

        url = URL(self.origin, self.headline_endpoint, query=query, aliases=self.aliases)
        url.append({'apiKey' : 'API_KEY'})
        self.assertEqual(url, expectedURL)
        return



if __name__ == '__main__':
    unittest.main()

