#!/usr/bin/env python3

# The following keys you need to get from Twitter: https://developer.twitter.com/en/apps
# NOTE: It is not good practice to store API-KEYS like this (We only do it for simplicity)
API_KEY = "The key you get from twitter"
API_SECRET = "The key you get from twitter"
ACCESS_TOKEN = "The key you get from twitter"
ACCESS_TOKEN_SECRET = "The key you get from twitter"

import tweepy
from datetime import datetime, timedelta, timezone
import schedule

OUR_SEARCH_TERMS = ['Python Programming', 'Numpy', 'Pandas Python', 'Pip Python','Python Software Foundation']

class PythonBot:
    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(auth)
        self.str_to_time = lambda x: datetime.strptime(x, '%a %b %d %H:%M:%S %z %Y')
        self.selection_function = lambda x: int(x['favorite_count']) + int(x['retweet_count'])
        self.last_tweet_time = datetime.now(timezone.utc) - timedelta(minutes=10)
        # run it once now and then every 10 minutes after that
        self.run_bot()
        schedule.every(10).minutes.do(self.run_bot)

    def run_bot(self):
        try:
            found_tweets = []
            for term in OUR_SEARCH_TERMS:
                found_tweets += self.api.search(term, lang='en', result_type='recent', count=1000)
            # remove the unneeded things
            found_tweets = [t._json for t in found_tweets]
            # make sure not to old
            found_tweets = [t for t in found_tweets if self.str_to_time(t['created_at']) > self.last_tweet_time]
            print(found_tweets)
            # make sure they contain a link/image/video
            found_tweets = [t for t in found_tweets if 'http' in t['text']]
            # make sure no retweets
            found_tweets = [t for t in found_tweets if not ('retweeted_status' in t)]
            # select most popular one
            tweet = max(found_tweets, key=self.selection_function)
            # let's retweet this one
            self.api.retweet(tweet['id'])
            self.last_tweet_time = datetime.now(timezone.utc)
            print(f"BOT SUCCESSFUL RUN AT {self.last_tweet_time}")
        except Exception as e:
            print("Houston we had a problem...", e)

if __name__ == '__main__':
    bot = PythonBot()
    while True:
        schedule.run_pending()