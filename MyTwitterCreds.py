__author__ = 'wlane'


class TwitterCreds:
    def __init__(self):
        self.consumer_key = 'mGoDFrFMV7zHV05rB8N9d2NFK'
        self.consumer_secret = 'D1v51YzhuGb2LhjOGwoz4sDjFuM5vqETatiYbyxlKly2g1pki0'
        self.oauth_token = '31221546-JOk6rEkpjCvHZYD7tO0JuUDVBW75hIqCOxPfPoQZj'
        self.oauth_secret = 'NiZIjkLEgA6MD6k8yEvd7mBJEd5Pkjn8z3Tgw2M5EIa6z'
        pass

    def getConsumerKey(self):
        return self.consumer_key

    def getConsumerSecret(self):
        return self.consumer_secret

    def getOAuthToken(self):
        return self.oauth_token

    def getOAuthSecret(self):
        return self.oauth_secret