'''
File: test_urlencoder.py

Brief: Unit tests for newsfeed urlencoder helper

Author: Alexander DuPree

'''
import unittest

from helpers.url import URL

class TestURLString(unittest.TestCase):

    origin = "https://newsapi.org/v2/"
    headline_endpoint = "top-headlines?"

    keys = ['country', 'keyword', 'category', 
            'source', 'apiKey', 'origin', 'endpoint']

    required = ['apiKey', 'origin', 'endpoint']

    ''' URL requires origin, endpoint, and apikey values '''
    def testRequiredSegments(self):
        payload = dict.fromkeys(self.keys)

        url = URL(self.origin, self.headline_endpoint, required=['apiKey'])
        with self.assertRaises(ValueError):
            url.encode(payload)


    ''' Sample valid News API query '''
    def testTopHeadlineRequest(self):

        query= ['us', 'harambe', 'business', 'cnn', 
                 'APIKEY', self.origin, self.headline_endpoint]

        payload = dict(zip(self.keys, query))

        expectedURL = (
                'https://newsapi.org/v2/top-headlines?'
                'country=us&'
                'q=harambe&'
                'category=business&'
                'sources=cnn&'
                'apiKey=API_KEY'
                )

        url = URL(self.origin, self.headline_endpoint)
        url.encode(payload)

        self.assertEqual(expectedURL, url)
        return

if __name__ == '__main__':
    unittest.main()

