import tweepy
import json

#Function that opens a file and stores the data into the file!
# def store_tweets(file, tweets):
#     with open(file, 'w') as f:
#         f.writelines(tweets)

#Setting up the twitter things!
access_token = '813887388938338304-LjJFQoLSHdLnLkRhPntQTMTapQ8gLSg'
access_token_secret = 'k6tofBjEIbW9mYX3rohITabsMn75SAFQczD1byIiK1HDY'
consumer_key = 'Gr3zy0a74Gt8Xf4tofm3UzeNF'
consumer_secret = '84u7UyDJ930Cfr2ho8lU0tQbChBTgvAXArWW1Vd2XbVyl9vOmT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = []
# pos_emojis = ['😙','❤','😍','💓','😗','☺','😊','😛','💕','😀','😃','😚']
# neg_emojis = ['☹','😕','😩','😒','😠','😐','😦','😣','😫','😖','😞','💔','😢','😟']

#all_emojis = pos_emojis + neg_emojis

#Stream for twitter
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweets.append(status.text.rstrip())
        if len(tweets) > 200:
            myStream.disconnect()


MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener)

myStream.filter(track=["black panther"], languages=['en'])

for x in tweets:
    print(x)
