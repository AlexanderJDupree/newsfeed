'''
File: formatter.py

Brief: Displays news API response in formatted console output

Author: Alexander DuPree

'''
import textwrap

def print_border():
    print("{}".format('-' * 80))

def format_into_string(article):
    return "{}\n{}\n{}\n{}\n".format(article['title'], 
                                     article['publishedAt'],
                                     article['description'], 
                                     article['url'])

def display_news(articles):
    for article in articles:
        display_article(article)
        print_border()
    return

def display_article(article):
    textWrapper = textwrap.dedent(format_into_string(article)).strip()
    print(textwrap.fill(textWrapper, width=80))
    return

def display_error(response):
    print("{}: {}\n{}".format(response['status'], 
                              response['code'], 
                              response['message']))
    return
