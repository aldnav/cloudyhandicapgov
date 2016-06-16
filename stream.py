import datetime
import json
import tweepy
import pprint
import dataset

# stores consumer key and secret, access token and token secret
from access import AuthAccess

private = AuthAccess()

POST_URL = 'http://192.168.1.39:5000/api/reports/'

db = dataset.connect('sqlite:///mydb.db')
table = db['tweets']


class StreamListener(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)

        geo = decoded['geo']

        if geo:
            s = decoded['timestamp_ms'] / 1000.0
            time = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
            data1 = {
                'location': decoded['geo']['coordinates'],
                'status': decoded['text'].encode('ascii', 'ignore'),
                'time': time,
                'name': decoded['screen_name'],
                'place': decoded['place']['full_name'],
            }
        #     print 'fuck', data1
        #     # requests.post(POST_URL, data=json.dumps(data1))

            # print json.dumps(decoded)
            table.insert(data1)
            print data1
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
