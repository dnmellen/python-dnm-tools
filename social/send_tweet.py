#!/usr/bin/python -tt

import sys
import tweepy

TWITTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""
TWITTER_ACCESS_TOKEN = ""
TWITTER_TOKEN_SECRET = ""


def tweet(msg):
    """
    Send a tweet with OAuth Authentication
    """

    # Get authenticated
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Debug
    print "Tweeting as " + api.me().name + ":" + msg

    # Send tweet
    api.update_status(msg)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        tweet(sys.argv[1])
    else:
        sys.stderr.write('No enough params\n')
        sys.exit(1)
