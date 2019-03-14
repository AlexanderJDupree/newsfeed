'''
File: urlencoder.py

Brief: urlencoder accepts a dictionary object and encodes it into a url query
       string

Author: Alexander DuPree

'''

import urllib.parse

class URL:

    def __init__(self, origin, endpoint, required=set()):
        self.origin = origin
        self.endpoint = endpoint
        self.required = set(required)

    def __validatePayload(self, payload):
        for key, value in payload.items():
            if key in self.required and value == None:
                raise ValueError
        return

    def encode(self, payload):
        self.__validatePayload(payload)
