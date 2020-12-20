import tweepy
import time

auth = tweepy.OAuthHandler('NZbvRXsvz9NznXGBUvTNEy2Y6',
                           'lIOSe3dtY1bxprR1m5DoRMaQaOOa2K1FiQRsI4ihaaeXltfJiN')
auth.set_access_token('895781968758980608-nt53Q3QRQKQ7gPTBkJnv0j9P8AzD6aI',
                      'zbG0jYPT30P0Fv1LQ4tfnT8I8AQcdPMsxfOY6spscv7xH')

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
