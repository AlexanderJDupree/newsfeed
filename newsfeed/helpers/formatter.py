'''
File: formatter.py

Brief: Displays news API response in formatted console output

Author: Alexander DuPree

'''
import textwrap

def _width():
    return 80

def _printBorder():
    print("{}".format('-' * _width()))

def _borderText(text):
    lines = text.splitlines()
    border = ['┌' + '─' * _width() + '┐']
    for line in lines:
        border.append('│' + (line + ' ' * _width())[:_width()] + '│')
    border.append('└' + '─' * _width() + '┘')
    return '\n'.join(border)

def _formatIntoString(article):
    header = "{}\nPublished At: {}\n".format(
             textwrap.fill(textwrap.dedent(article['title']), width=_width()),
             article['publishedAt'] # TODO format datetime string
             )
    body = "\n{}\n\n{}".format(
             '\n'.join(textwrap.wrap(article['description'], width=_width())),
             textwrap.fill(textwrap.dedent(article['url']), width=_width())
             )
    return header + '─' * _width() + body

def displayNews(articles):
    for article in articles:
        displayArticle(article)
    return

def displayArticle(article):
    print(_borderText(_formatIntoString(article)))
    return

def displayError(response):
    header = "{}: {}\n".format(response['status'], response['code'])
    body = "\n{}".format('\n'.join(textwrap.wrap(response['message'])))
    print(_borderText(header + '─' * _width() + body))
    return
