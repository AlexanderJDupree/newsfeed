#!/usr/bin/python

'''
usage: newsfeed.py [-h] [-t] [-c]

Get your news without having to leave the terminal!

optional arguments:
  -h, --help       show this help message and exit
  -t , --top       Display top <N> stories
  -c , --country   Filter news by <COUNTRY>
  -k , --keyword   Filter news for a specified <KEYWORD>
  -C , --category  Filter news within a specified <CATEGORY>
  -s , --sources   Specify a <SOURCE> for news. I.E. cnn, bbc-news

  Note: sources parameter is not implemented yet in v1.0.0!

'''

__version__ = 'v1.0.0'

from os import sys
from helpers import formatter, commandParser
from helpers.newsAPI import NewsAPI

def main(argv):

    exit_code = 0

    query = commandParser.parse(argv)

    response = NewsAPI.request(query)

    if response['status'] != 'ok':
        formatter.displayError(response)
        exit_code = 1
    elif len(response['articles']) == 0:
        displayNoResultsFound(query)
    else:
        formatter.displayNews(response['articles'])

    displayCredits()
    return exit_code

def displayNoResultsFound(query):
    print("\nSorry, No results found for query:\n\t", end='')
    for key, val in query.items():
        print("{}:{}  ".format(key.upper(), val), end='')

    # TODO print out a list of country codes and categories
    print('\n\nSee https://newsapi.org/docs for a list of country codes and categories')
    return

def displayCredits():
    print("\n{0:^{4}}\n{1:^{4}}\n{2:^{4}}\n{3:^{4}}".format(
        "Powered by News API (https://newsapi.org)",
        "Contribute to make newsfeed better!",
        "https://github.com/AlexanderJDupree/newsfeed",
        __version__,
        formatter._width()))

if __name__ == '__main__':
    main(sys.argv[1:])
