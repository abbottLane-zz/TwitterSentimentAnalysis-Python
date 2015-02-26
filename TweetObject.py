__author__ = 'wlane'


class TweetObject:
    def __init__(self, tweet, positivity, retweets):
        self.tweet = tweet
        self.positivity = positivity
        self.retweets = retweets
        pass

    def get_positivity(self):
        return self.positivity

    def get_tweet_text(self):
        return self.tweet

    def get_retweets(self):
        return self.retweets


