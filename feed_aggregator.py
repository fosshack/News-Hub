
feeds = [
    'http://www.sfgate.com/rss/feed/Tech-News-449.php',
    'http://feeds.feedburner.com/TechCrunch/startups',
    'http://news.cnet.com/8300-1001_3-92.xml',
    'http://www.zdnet.com/news/rss.xml',
    'http://www.computerweekly.com/rss/Latest-IT-news.xml',
    'http://feeds.reuters.com/reuters/technologyNews',
    'http://www.tweaktown.com/news-feed/'
]

import feedparser
import nltk
from bs4 import BeautifulSoup

corpus = []
titles = []
ct = -1
for feed in feeds:
    d = feedparser.parse(feed)
    for e in d['entries']:
        soup = BeautifulSoup(e['description'])
        words = nltk.wordpunct_tokenize(soup.get_text())
        words.extend(nltk.wordpunct_tokenize(e['title']))
        lowerwords = [x.lower() for x in words if len(x) > 1]
        ct += 1
        print ct, "TITLE", e['title']
        corpus.append(lowerwords)
        titles.append(e['title'])


import math
from operator import itemgetter


def freq(word, document): return document.count(word)


def wordCount(document): return len(document)


def numDocsContaining(word, documentList):
    count = 0
    for document in documentList:
        if freq(word, document) > 0:
            count += 1
    return count


def tf(word, document): return (freq(word, document) / float(wordCount(document)))


def idf(word, documentList): return math.log(len(documentList) / numDocsContaining(word, documentList))


def tfidf(word, document, documentList): return (tf(word, document) * idf(word, documentList))


import operator


def top_keywords(n, doc, corpus):
    d = {}
    for word in set(doc):
        d[word] = tfidf(word, doc, corpus)
    sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))
    sorted_d.reverse()
    return [w[0] for w in sorted_d[:n]]


key_word_list = set()
nkeywords = 4
[[key_word_list.add(x) for x in top_keywords(nkeywords, doc, corpus)] for doc in corpus]

ct = -1
for doc in corpus:
    ct += 1
    print ct, "KEYWORDS", " ".join(top_keywords(nkeywords, doc, corpus))