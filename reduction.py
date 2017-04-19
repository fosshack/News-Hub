#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from twitter_lib import TwitterClient

dict = {'NN': 'NOUN', 'JJ': 'ADJ'}
dict['NNS'] = 'NOUN'
dict['NNP'] = 'NOUN'
dict['NNPS'] = 'NOUN'
dict['PRP'] = 'NOUN'
dict['PRP$'] = 'NOUN'
dict['RB'] = 'ADV'
dict['RBR'] = 'ADV'
dict['RBS'] = 'ADV'
dict['VB'] = 'VERB'
dict['VBD'] = 'VERB'
dict['VBG'] = 'VERB'
dict['VBN'] = 'VERB'
dict['VBP'] = 'VERB'
dict['VBZ'] = 'VERB'
dict['WRB'] = 'ADV'


def reduce(sentence):
    sentence = sentence.lower()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sentence)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    # print filtered_sentence

    temp = nltk.pos_tag(filtered_sentence)

    # print temp

    # twitter_obj = TwitterClient()
    #
    # for i in temp:
    #     tweets = twitter_obj.get_tweets(query=i,count=200)
    #     if tweets:
    #         ptweets = [t for t in tweets if t['sentiment'] == "positive"]
    #         ntweets = [t for t in tweets if t['sentiment'] == "negative"]
    #
    #         print "Positive tweets \n\n"
    #         for tweet in ptweets[:10]:
    #             print tweet['text']
    #
    #         print "\n\nNegative tweets"
    #         for tweet in ntweets[:10]:
    #             print tweet['text']



    new_sentence = ''

    print temp

    for i in temp:
        try:
            k = i[1]
            if dict[k] != None:
                part_speech = dict[k]
            else:
                part_speech = 'NOUN'  # default is noun

            if part_speech == 'NOUN':
                word = wn.morphy(i[0], wn.NOUN)
            elif part_speech == 'VERB':

                # word = ""

                word = wn.morphy(i[0], wn.VERB)
            elif part_speech == 'ADV':

                # word = ""

                word = wn.morphy(i[0], wn.ADV)
            elif part_speech == 'ADJ':

                # word = ""

                word = wn.morphy(i[0], wn.ADJ)

                # print word

            word1 = wn.synsets(word)[0].lemmas()[0].name()
        except:
            word1 = i[0]
        if new_sentence == '':
            new_sentence = new_sentence + word1.lower()
        else:
            new_sentence = new_sentence + ' ' + word1.lower()

    return new_sentence

# print reduce("Shah Rukh Khan honoured in San Francisco")