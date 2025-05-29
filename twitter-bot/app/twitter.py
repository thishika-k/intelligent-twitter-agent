import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)

api = tweepy.API(auth)

def fetch_mentions(since_id=None):
    return api.mentions_timeline(since_id=since_id, tweet_mode='extended')

def post_reply(text, reply_to_status_id):
    api.update_status(status=text, in_reply_to_status_id=reply_to_status_id, auto_populate_reply_metadata=True)