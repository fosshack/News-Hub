from constants import NEWS_API_BASE_URL, NEWS_API_KEY
import requests
import json


# retrieves and get the news from a particular source.
class _news():

    def get_json(self,source):
        new_payload = {
            'source' : source,
            'sortBy' : 'latest',
            'apiKey' : NEWS_API_KEY
        }
        rsp = requests.get(NEWS_API_BASE_URL, params=new_payload)
        news_json = json.loads(rsp.text)
        return news_json

