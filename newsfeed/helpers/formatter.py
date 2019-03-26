'''
File: formatter.py

Brief: Displays news API response in formatted card output

Author: Alexander DuPree

'''
import textwrap
from termcolor import colored

def _width():
    return 80 # TODO make width dynamic to terminal size

def _borderText(text, color='white', attrs=[]):
    result = [ '│ {}'.format(colored(line, color, attrs=attrs)) 
               + ' ' * (_width() - len(line)) + ' │'
               for line in textwrap.wrap(text, _width()) ]
    return '\n'.join(result)

def _wrapText(text):
    return '\n'.join(textwrap.wrap(text, width= _width()))

def _formatIntoCard(article):

    topBorder = '┌' + '─' * (_width() + 2) + '┐\n'
    bottomBorder = '\n└' + '─' * (_width() + 2) + '┘'

    title = _borderText(article['title'], attrs=['bold'])
    # TODO format datetime string into MM-DD-YY:local time
    date = '\n' + _borderText("Published At: {}".format(article['publishedAt']), 'green')
    
    description = '\n' + _borderText(article['description'])
    url = '\n' + _borderText(article['url'], 'cyan', attrs=['underline'])

    return ( topBorder 
           + title 
           + date 
           + '\n' 
           + _borderText('─' * _width(), attrs=['bold']) 
           + description 
           + url 
           + bottomBorder)

def _cleanArticle(article):
    ''' Replaces any None objects with an empty string '''
    for attribute in [ 'title', 'publishedAt', 'description', 'url' ]:
        if article[attribute] == None:
            article[attribute] = ' '
    return 

def displayNews(articles):
    for article in articles:
        _cleanArticle(article)
        displayArticle(article)
    return

def displayArticle(article):
    print(_formatIntoCard(article))
    return

def displayError(response):
    header = "{}: {}\n".format(
            colored(response['status'], 'red'), 
            colored(response['code'], 'yellow', attrs=['bold'])
            )
    body = "\n{}".format(_wrapText(response['message']))
    print(header + '─' * _width() + body)
    return

