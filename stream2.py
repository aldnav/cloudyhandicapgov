
import os
import json
import datetime
import pprint

import dataset
from twitter import Api

CONSUMER_KEY = 'gJovjHOGuxRsvHAfCfxaNtwPf'
CONSUMER_SECRET = 'ODFTgSUrHFHymGjh2LSyMFX9DQQXuKiBHMn51008xeGLcU0kRv'
ACCESS_TOKEN = '242746743-Qiqe39fCVdd5YdDXUtaFPWadB47E3Wmjmr9lUnyp'
ACCESS_TOKEN_SECRET = 'uchoBIMD9NgaUtc6qqDcJUHlsPHN9Y0YNEwNgU80hhUuV'

api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)

db = dataset.connect('sqlite:///mydb.db')
table = db['tweets']


def main():
    # with open('output.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
    pp = pprint.PrettyPrinter()
    for line in api.GetStreamFilter(track=['accident'],
                                    locations=['116.87,5.62,128.44,19.68']):
        decoded = line
        pp.pprint(decoded)
        geo = decoded['geo']
        if geo:
            s = float(decoded['timestamp_ms']) / 1000.0
            time = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
            data1 = {
                'location': str(decoded['geo']['coordinates']),
                'status': decoded['text'].encode('ascii', 'ignore'),
                'time': time,
                'name': decoded['user']['screen_name'],
                'place': str(decoded['place']['full_name']),
            }
            print data1
            table.insert(data1)


if __name__ == '__main__':
    main()
