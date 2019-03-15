'''

File: commandParser.py

Brief: Parses command line args into a dict object and validates input

Author: Alexander DuPree

'''

import argparse

def validateInteger(string):
    value = int(string)
    if value < 1 or value > 100:
        raise argparse.ArgumentTypeError(
                '{} is not within range 1..100'.format(string)
                )
    return string

def parse(argv):

    parser = argparse.ArgumentParser(
            description="Get your news without having to leave the terminal!"
            )

    parser.add_argument(
            '-t', '--top', 
            type=validateInteger, 
            metavar='',
            default='10',
            help='Display top <N> stories. Range 1 - 100'
            )
    parser.add_argument(
            '-c', '--country',
            metavar='',
            default='us',
            help='Filter news by <COUNTRY>'
            )
    parser.add_argument(
            '-k', '--keyword',
            metavar='',
            help='Filter news for a specified <KEYWORD>'
            )
    parser.add_argument(
            '-C', '--category',
            metavar='',
            help="Filter news within a specified <CATEGORY>"
            )
    parser.add_argument( # TODO make sources accept variable number of args
            '-s', '--sources',
            metavar='',
            help="Specify a <SOURCE> for news. I.E. cnn, bbc-news"
            )

    # Returns a dict object
    return vars(parser.parse_args(argv))

