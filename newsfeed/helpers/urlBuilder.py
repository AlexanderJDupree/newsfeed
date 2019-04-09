'''
File: urlBuilder.py

Brief: urlencoder accepts a dictionary object and encodes it into a url query
       string

Author: Alexander DuPree

'''

from urllib import parse

class URL:
    ''' 
    URL class provides basic methods to build a url request by providing required 
    components in the form of a dict object. Optionally required compononets can be 
    specified during construction as well.
    '''

    def __init__(self, origin, endpoint, required=set(), query=dict(), aliases=dict()):
        self.origin   = origin
        self.endpoint = endpoint
        self.required = set(required)
        self.aliases  = aliases
        self.encode(query)

    def encode(self, query):
        ''' Constructs the URL string '''
        self.query = self.__encodeQuery(query) if query else ''
        self.url = self.origin + self.endpoint + self.query
        return

    # TODO D.R.Y. Violation from encode method
    def append(self, query):
        ''' Appends query to current query '''
        self.query += '&' + self.__encodeQuery(query) if query else ''
        self.url = self.origin + self.endpoint + self.query
        return

    def __encodeQuery(self, query):
        ''' Converts query dict object into a query string  '''
        self.__validateQuery(query)

        return parse.urlencode(self.__aliasQuery(query))
        
    def __validateQuery(self, query):
        for key in self.required:
            if key not in query or query[key] == None:
                raise ValueError # TODO Make custom exception
        return

    def __aliasQuery(self, query):
        ''' Alias the keys in the query to the specified aliases '''

        alias = { k : v for k, v in query.items() if v != None }
        for key in self.aliases.keys():
            if key in alias:
                alias[self.aliases[key]] = alias.pop(key)
        return alias

    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other

    def __lt__(self, other):
        return self.url < other

    def __hash__(self):
        return hash(self.url)

