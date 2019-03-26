'''
File: test_formatter.py

Brief: Unit tests for newsfeed formatter helper

Author: Alexander DuPree

'''
import unittest
from helpers import formatter

class TestFormatter(unittest.TestCase):


    # TODO create sample expected values for testing
    def testBorderTextWidth(self):
        expected = '│ \x1b[37maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x1b[0m │'
        self.assertEqual(formatter._borderText('a' * 80), expected)
 
    def testBorderTextLTWidth(self):
        expected = '│ \x1b[37maaaaaaaaaa\x1b[0m                                                                       │'
        self.assertEqual(formatter._borderText('a' * 10), expected)

    def testBorderTextGTWidth(self):
        expected = '│ \x1b[37maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x1b[0m │\n│ \x1b[37maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x1b[0m │\n│ \x1b[37maaaaaaaaaaaaaaa\x1b[0m                                                                  │' 
        self.assertEqual(formatter._borderText('a' * 175), expected)

    def testFormatIntoCard(self):
        pass # TODO create sample articles file for testing

    def testCleanArticle(self):
        expected = {
                'title' : ' ', 
                'publishedAt' : ' ', 
                'description' : ' ', 
                'url' : ' '}
        article = {
                'title' : None, 
                'publishedAt' : None, 
                'description' : None, 
                'url' : None 
                }

        formatter._cleanArticle(article)

        self.assertEqual(article, expected)
        pass

if __name__ == '__main__':
    unittest.main()

