# coding=utf-8
import sys
from textblob import TextBlob
from TweetObject import TweetObject
import TweetScraper
import twitter
import matplotlib
import pylab
from scipy.stats.stats import pearsonr

__author__ = 'wlane'

CONSUMER_KEY = 'mGoDFrFMV7zHV05rB8N9d2NFK'
CONSUMER_SECRET = 'D1v51YzhuGb2LhjOGwoz4sDjFuM5vqETatiYbyxlKly2g1pki0'
OAUTH_TOKEN = '31221546-JOk6rEkpjCvHZYD7tO0JuUDVBW75hIqCOxPfPoQZj'
OAUTH_TOKEN_SECRET = 'NiZIjkLEgA6MD6k8yEvd7mBJEd5Pkjn8z3Tgw2M5EIa6z'

# pull argument[0] from cmd line: this is our query string
query = str(sys.argv[1])

# Authorization to use twitter api
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Use twitter-api object to make calls to twitter
twitter_api = twitter.Twitter(auth=auth)

# create TweetScraper Object
obj = TweetScraper.TweetScraper()

# use tweetScraper obj to collect the tweets, store them in rawArray
rawArray = obj.scrape_twitter_timeline(twitter_api, query)

# open file to write all tweets to text file (Data dump)
txtFile = open("tweets.txt", 'w')
count = 0

# read text file
tweetArray = []
for tweet in rawArray:
    text = tweet['text']
    blob = TextBlob(text)
    count += 1

    # Create array of tweet objects
    tweetArray.append(TweetObject(tweet['text'].encode('utf-8'), str(blob.sentiment.polarity), tweet['retweet_count'],
                                  tweet['user']['name']))

    # Write raw data to file
    txtFile.write(str(count) + ": " + tweet['text'].encode('utf-8') + "\n\t" + str(blob.sentiment) + "\n")


print "Sentiment and tweets recorded in tweets.txt"
print ""
print "calculating correlation between positivity score and number of retweets ..."

positivityList = []
retweetList = []
mostPositiveTweet = TweetObject("tweet", 0, 0, "wlane")
mostNegativeTweet = TweetObject("tweet", 0, 0, "wlane")
mostRetweetedTweet = TweetObject("tweet", 0, 0, "wlane")

for tweet in tweetArray:
    positivityList.append(float(tweet.get_positivity()))
    retweetList.append(float(tweet.get_retweets()))
    if float(tweet.get_positivity()) > float(mostPositiveTweet.get_positivity()):
        mostPositiveTweet = tweet
    if float(tweet.get_positivity()) < float(mostNegativeTweet.get_positivity()):
        mostNegativeTweet = tweet
    if int(tweet.get_retweets()) > int(mostRetweetedTweet.get_retweets()):
        mostRetweetedTweet = tweet

print ""
print "--------------------------------------------------"
print "#######      Results      ########################"
print "--------------------------------------------------"
print ""
print "Most Positive Tweet: \n" + "   " + mostPositiveTweet.get_tweet_text()
print "   Positivity Score: " + str(mostPositiveTweet.get_positivity())
print "   Retweets: " + str(mostPositiveTweet.get_retweets())
print ""
print "Most Negative Tweet: \n" + "   " + mostNegativeTweet.get_tweet_text()
print "   Positivity Score: " + str(mostNegativeTweet.get_positivity())
print "   Retweets: " + str(mostNegativeTweet.get_retweets())
print ""
print "Most Retweeted Tweet: \n" + "   " + mostRetweetedTweet.get_tweet_text()
print "   Positivity Score: " + str(mostRetweetedTweet.get_positivity())
print "   Retweets: " + str(mostRetweetedTweet.get_retweets())

# as the positivity score gets bigger, the number of retweets goes down for negative corr, or up for pos corr
correlation = pearsonr(retweetList, positivityList)
print "Correlation, p-value: " + str(correlation)
print ""
print "  ¯\_(ツ)_/¯ "
print ""
print "####################################################"

print ""
print "producing scatterplot ... "


matplotlib.pyplot.scatter(retweetList, positivityList)
matplotlib.pyplot.show()




