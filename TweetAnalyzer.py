import sys
from paste.util.quoting import default_encoding
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
    tweetArray.append(TweetObject(tweet['text'].encode('utf-8'), str(blob.sentiment.polarity), tweet['retweet_count'],
                                  tweet['user']['name']))

    # Write raw data to file
    txtFile.write(str(count) + ": " + tweet['text'].encode('utf-8') + "\n\t" + str(blob.sentiment) + "\n")

# print blob.tags
print "Sentiment and tweets recorded in tweets.txt"
print ""
print "calculating correlation between positivity score and number of retweets ..."

positivityList = []
retweetList = []
mostPositiveTweet = TweetObject("tweet", 0, 0, "wlane")
mostNegativeTweet = TweetObject("tweet", 0, 0, "wlane")
for tweet in tweetArray:
    positivityList.append(float(tweet.get_positivity()))
    retweetList.append(float(tweet.get_retweets()))
    if tweet.get_positivity() > mostPositiveTweet.get_positivity():
        mostPositiveTweet = tweet
    if tweet.get_positivity() < mostNegativeTweet.get_positivity():
        mostNegativeTweet = tweet

print ""
print "Most Positive Tweet: \n" + "   " + mostPositiveTweet.get_tweet_text()
print "   Positivity Score: " + str(mostPositiveTweet.get_positivity())
print "   Retweets: " + str(mostPositiveTweet.get_retweets())
print ""
print "Most Negative Tweet: \n" + "   " + mostNegativeTweet.get_tweet_text()
print "   Positivity Score: " + str(mostNegativeTweet.get_positivity())
print "   Retweets: " + str(mostNegativeTweet.get_retweets())
print ""

# as the positivity score gets bigger, the number of retweets goes down for negative corr, or up for pos corr
correlation = pearsonr(retweetList, positivityList)
print "Correlation, p-value: " + str(correlation)

print ""
print "producing scatterplot ... "

matplotlib.pyplot.scatter(retweetList, positivityList)
matplotlib.pyplot.show()


# print "\n\nTESTS: \nPositivity Sample: " + tweetArray[3].get_positivity() + " \n The Tweet: " + tweetArray[
#     3].get_tweet_text() + "\n Retweet Count: " + str(tweetArray[3].get_retweets()) + "\nUser: " + tweetArray[
#     3].get_screen_name()

