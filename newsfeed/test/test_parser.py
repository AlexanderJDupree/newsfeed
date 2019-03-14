'''
File: test_parser.py

Brief: Unit tests for newsfeed parser helper

Author: Alexander DuPree

'''
import unittest
import argparse

from helpers import parser

class TestMainParser(unittest.TestCase):

    ''' Command line options '''
    options = ['top', 'country', 'keyword', 'category', 'source']
    longopts = [ '{}{}'.format('--', option) for option in options ]

    ''' Default options are to display top 10 US Stories'''
    def testDefaultOptions(self):

        expectedDict = dict(zip(self.options, ['10', 'us', None, None, None]))

        self.assertEqual(expectedDict, parser.parse([]))

    ''' Out of bounds -t/--top option raises exception '''
    def testTopOptionBounds(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parser.validateInteger("101")
        with self.assertRaises(argparse.ArgumentTypeError):
            parser.validateInteger("0")

    def testCompositeOptions(self):
        expectedValues = ['42', 'ar', 'beer', 'technology', 'bbc-news']
        expectedDict = dict(zip(self.options, expectedValues))

        # [--top, 42, --country, us, ... --source, bbc-news]
        testArgv = [arg for opt in zip(self.longopts, expectedValues) for arg in opt]

        self.assertEqual(expectedDict, parser.parse(testArgv))

if __name__ == '__main__':
    unittest.main()

