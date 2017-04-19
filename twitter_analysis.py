from tweet import twit_search
import json
from newsapi import _news


def get_json_data(source):
    p_percentage = 0
    n_percentage = 0
    neutral_percentage = 0

    news_obj = _news()
    news_dict = news_obj.get_json(source)

    print news_dict

    news_new_dict = {}
    news_new_list = []

    for news in news_dict['articles']:
        temp = {}

        # print news['title']
        title = reduce(news['title'])
        print title
        tweets = twit_search(title)
        if tweets:
            ptweets = [t for t in tweets if t['sentiment'] == "positive"]
            ntweets = [t for t in tweets if t['sentiment'] == "negative"]
            p_percentage = format(100 * len(ptweets) / len(tweets))
            n_percentage = format(100 * len(ntweets) / len(tweets))
            neutral_percentage = format(100 * (len(tweets) - len(ntweets) - len(ptweets))/len(tweets))

            temp['p_percentage'] = p_percentage
            temp['n_percentage'] = n_percentage
            temp['neutral_percentage'] = neutral_percentage

            news_new_list.append(temp)

            # print p_percentage
            # print n_percentage
            # print neutral_percentage
        else:
            temp['p_percentage'] = p_percentage
            temp['n_percentage'] = n_percentage
            temp['neutral_percentage'] = neutral_percentage

            news_new_list.append(temp)

            print p_percentage
            print n_percentage
            print neutral_percentage

    # print news_new_list
    news_new_dict = {'response':news_new_list}