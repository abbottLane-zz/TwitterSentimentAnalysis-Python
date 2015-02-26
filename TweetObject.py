__author__ = 'wlane'


class TweetObject:
    def __init__(self, tweet, positivity, retweets, screen_name):
        self.tweet = tweet
        self.positivity = positivity
        self.retweets = retweets
        self.screen_name = screen_name
        pass

    def get_positivity(self):
        return self.positivity

    def get_tweet_text(self):
        return self.tweet

    def get_retweets(self):
        return self.retweets

    def get_screen_name(self):
        return self.screen_name
