'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
for tweet in tweetData:
    text = tweet["text"]
    #print(tweet["text"])
    blob = TextBlob(text)
    print(blob.polarity)
    #print(text["polarity"])


## json object or tweets are store in tweetData

#iterate list of tweets_small
    #for each tweet access the text. Use the text field tweet.textb
    #print polarity



# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
