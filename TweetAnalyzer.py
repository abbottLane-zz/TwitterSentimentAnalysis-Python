import sys
from paste.util.quoting import default_encoding
from textblob import TextBlob
from TweetObject import TweetObject
import TweetScraper
import twitter

__author__ = 'wlane'

CONSUMER_KEY = 'mGoDFrFMV7zHV05rB8N9d2NFK'
CONSUMER_SECRET = 'D1v51YzhuGb2LhjOGwoz4sDjFuM5vqETatiYbyxlKly2g1pki0'
OAUTH_TOKEN = '31221546-JOk6rEkpjCvHZYD7tO0JuUDVBW75hIqCOxPfPoQZj'
OAUTH_TOKEN_SECRET = 'NiZIjkLEgA6MD6k8yEvd7mBJEd5Pkjn8z3Tgw2M5EIa6z'

# pull argument[0] from cmd line: this is our query string
query = str(sys.argv[1])
print "query is : " + query

# Authorization to use twitter api
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Use twitter-api object to make calls to twitter
twitter_api = twitter.Twitter(auth=auth)

# scrape tweets and create tweets.txt file
obj = TweetScraper.TweetScraper()
rawArray = obj.scrape_twitter(twitter_api, query)

# open file to write all tweets to text file
txtFile = open("tweets.txt", 'w')
count = 0

# read text file
tweetArray = []
for tweet in rawArray:
    text = tweet['text']
    blob = TextBlob(text)
    count += 1

    # Create array of tweet objects
    tweetArray.append(TweetObject(tweet['text'].encode('utf-8'), str(blob.sentiment.polarity)))

    # Write raw data to file
    txtFile.write(str(count) + ": " + tweet['text'].encode('utf-8') + "\n\t" + str(blob.sentiment) + "\n")

# print blob.tags
print "Sentiment and tweets recorded in tweets.txt"
print "Positivity Sample: " + tweetArray[0].get_positivity() + " The Tweet: " + tweetArray[0].get_tweet_text()

