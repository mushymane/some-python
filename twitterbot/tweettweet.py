import tweepy
import time

auth = tweepy.OAuthHandler('api_token',
                           'api_secret_key')
auth.set_access_token('access_token',
                      'access_secret')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'blackpink'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     break
