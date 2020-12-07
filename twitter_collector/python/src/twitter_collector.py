from twython import TwythonStreamer
import json
from datetime import datetime

# from https://stackabuse.com/accessing-the-twitter-api-with-python/

# config
keyword = "crisis"

# Create a class that inherits TwythonStreamer
class TwitterStreamer(TwythonStreamer):     

    # Received data
    def on_success(self, data):
        self.save_as_json(data)
        #print("tweet " + str(len(data)) + "fields, " + str(datetime.now()))

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
    # Save each tweet to csv file
    def save_as_json(self, tweet):
        with open(r'/app/{}_tweets_{}.json'.format(keyword, datetime.now().strftime('%Y%m%d')), 'a') as file:
            json.dump(tweet, file) 
            file.write('\n')
            file.close()

# Load credentials from json file
with open("twitter_credentials.json", "r") as creds_file:
    creds = json.load(creds_file)

# Instantiate from our streaming class
stream = TwitterStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
# Start the stream
stream.statuses.filter(track=keyword)

