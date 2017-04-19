#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import the necessary package to process data in JSON format

try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API

ACCESS_TOKEN = '241418788-KNAZ24hT7qgImCMrUMrFK3AgngWUa2Nnct8S0KVO'
ACCESS_SECRET = 'gCGG0XQ0wLrIDxAJl4ga0xjp7256UH2xGjoZu5h49Jb7R'
CONSUMER_KEY = 'DJYd7k0qRK2YUe3gZH3tmVhdl'
CONSUMER_SECRET = '03KBCi4J81lpxDNxjkcx77Fg7IhX3HiW2TPHNEEcIjlbPzxE7p'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY,
              CONSUMER_SECRET)


# Initiate the connection to Twitter Streaming API

def twit_search(query):
    search_query = query.replace(' ', '%20')
    twitter_stream = TwitterStream(auth=oauth)
    twitter = Twitter(auth=oauth)
    search_data = twitter.search.tweets(q=search_query,
                                        result_type='recent', lang='en', count=10)
    with open('data.txt', 'w') as outfile:
        json.dump(search_data, outfile)
    return json.dumps(search_data)