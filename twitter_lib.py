import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from constants import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, \
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET


class TwitterClient(object):

    def __init__(self):

        # Twitter auth keys
        consumer_key = TWITTER_CONSUMER_KEY
        consumer_secret = TWITTER_CONSUMER_SECRET
        access_token = TWITTER_ACCESS_TOKEN
        access_token_secret = TWITTER_ACCESS_TOKEN_SECRET

        # attempt authentication

        try:

            # create OAuthHandler object

            self.auth = OAuthHandler(consumer_key, consumer_secret)

            # set access token and secret

            self.auth.set_access_token(access_token,
                                       access_token_secret)

            # create tweepy API object to fetch tweets

            self.api = tweepy.API(self.auth)
        except:
            print 'Error: Authentication Failed'

    def clean_tweet(self, tweet):

        # function to clean the tweets from links and other unwanted characters
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
                               , ' ', tweet).split())

    def get_tweet_sentiment(self, tweet):

        # Utility function to get the sentiment using the sentiment analysis provided by
        # the TextBlob

        # create TextBlob object of passed tweet text

        analysis = TextBlob(self.clean_tweet(tweet))

        # set sentiment

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        # Main function to fetch tweets and parse them

        # empty list to store parsed tweets

        tweets = []

        try:

            # call twitter api to fetch tweets

            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one

            for tweet in fetched_tweets:

                # empty dictionary to store required params of a tweet

                parsed_tweet = {}

                # saving text of tweet

                parsed_tweet['text'] = tweet.text

                # saving sentiment of tweet

                parsed_tweet['sentiment'] = \
                    self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list

                if tweet.retweet_count > 0:

                    # if tweet has retweets, ensure that it is appended only once

                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets

            return tweets
        except tweepy.TweepError, e:

            # print error (if any)

            print 'Error : ' + str(e)