import json
import tweepy
from tweepy import OAuthHandler


# Twitter's consumer authentication keys and tokens
CONSUMER_KEY = 'DimUYgwtB5qtMjzIHTFKf7XWr'
CONSUMER_SECRET = 'F1qWEMWq29IZRwlkg5M4HpBMKKKtqL7LIcFbWOwQa4siQJp2lA'
OAUTH_TOKEN = '334017514-Ri2ooUt1uwkL0k7otueSxBTzBmxWeLaPnYM3LC8m'
OAUTH_TOKEN_SECRET = 'nMZ1vLgqJOCfjlNZ8JGTeZ4pFlpR3hvtwHmXrucEqEywP'


# Create instance of Tweepy OAuthHandler class and assign it to the 'auth' variable.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# Invoke the 'set_access_token' function passing in the OAuth token and the OAuth token secret values as arguments.
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# Create an instace of Twitter API that will do the actual data access.
# In order for Twitter to allow the access to the API you pass in the OAuth handler object.
api = tweepy.API(auth)


# Create Dublin's "Where on Earth Identifier"(WOEID) variable.
DUB_WOE_ID = 560743


# Invoke the 'trends_place' Tweepy API method passing in the 'DUB_WOE_ID' variable as an argument and assign it to the 'dub_trends' variable.
dub_trends = api.trends_place(DUB_WOE_ID)


# Print results to the console.
print(json.dumps(dub_trends, indent=1))
