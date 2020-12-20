import tweepy
import time

auth = tweepy.OAuthHandler('PDkCXxxBRbB2gEreFUq4vX99c',
                           'S4TV5hIcvmLHav5BYbjI4RDOHqPiKTR3Wcqp963I9FFS3738Kr')
auth.set_access_token('895781968758980608-3iaRoQbaV5Scga3fXb2UMR0FcC5HRhP',
                      'bEkDO64FIYiCI79NWnmkvuA0nR7PsNtmb1erkQqQAxTmB')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    # if follower.name == '':
    follower.follow()
    break
    # print(follower.name)
