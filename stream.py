import datetime
import json
import tweepy
import pprint

# stores consumer key and secret, access token and token secret
from access import AuthAccess

private = AuthAccess()

class StreamListener(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)

        geo = decoded['geo']

        if geo:
            # print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))

            pp = pprint.PrettyPrinter(indent=2)
            pp.pprint(decoded)

            # with open('arrow', 'ab') as sample_file:
            #     sample_file.write(json.dumps(decoded) + '\n')

        return True

    def on_error(self, status):
        print(status)


def start_stream(auth, listener):
    while(True):
        try:
            stream = tweepy.Stream(auth, listener)
            stream.filter(locations=[116.87,5.62,128.44,19.68], track=['accident'])
        except: # catch every error and just restart
            pass


if __name__ == '__main__':
    listener = StreamListener()
    auth = tweepy.OAuthHandler(private.consumer_key, private.consumer_secret)
    auth.set_access_token(private.access_token, private.access_token_secret)

    print("Now streaming tweets from the Philippines")
    start_stream(auth, listener)
