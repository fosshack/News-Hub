from textblob import TextBlob


def analyse(sentence):
    text = TextBlob(sentence)
    if text.polarity < 0:
        print "negative"
    elif text.polarity == 0:
        print "neutral"
    else:
        print "positive"
    # print text.polarity
    # print text.subjectivity

# analyse("This is ridiculous,")