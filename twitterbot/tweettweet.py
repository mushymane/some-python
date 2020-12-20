import tweepy

auth = tweepy.OAuthHandler('PDkCXxxBRbB2gEreFUq4vX99c',
                           'S4TV5hIcvmLHav5BYbjI4RDOHqPiKTR3Wcqp963I9FFS3738Kr')
auth.set_access_token('895781968758980608-3iaRoQbaV5Scga3fXb2UMR0FcC5HRhP',
                      'bEkDO64FIYiCI79NWnmkvuA0nR7PsNtmb1erkQqQAxTmB')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
