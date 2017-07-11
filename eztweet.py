#!/usr/bin/python

#credit to Tweepy library. Made this really easy
#Code by Joel Sacco
#Use this to add the ability to tweet to other scripts / cron jobs / whatever 

# syntax is : python eztweet.py "here is a tweet the text goes here"
# will print out a confirmation after  

import tweepy
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("tweet", help="what you wish to tweet")
args = parser.parse_args()

tweetext = args.tweet
tweetime = time.strftime("%A, %B %d, %Y %I:%M:%S %p")

# get the below info from dev.twitter.com or something

class TwitterAPI:
    def __init__(self):
        consumer_key = "YOURCONSUMERKEY"
        consumer_secret = "YOURCONSUMERSECRET"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "YOURACCESSTOKEN"
        access_token_secret = "YOURACCESSTOKENSECRET"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(tweetext)
    print "Tweet Posted at %s: %s" % (tweetime, tweetext)
