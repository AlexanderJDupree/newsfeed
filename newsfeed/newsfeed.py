import os
import secret
import requests

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=' + secret.NEWS_API_KEY)
response = requests.get(url)
print(response.json())

