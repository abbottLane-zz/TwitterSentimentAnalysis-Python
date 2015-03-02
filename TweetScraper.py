__author__ = 'wlane'


class TweetScraper:
    def __init__(self):
        pass

    # Returns a count of how many tweets were collected
    @staticmethod
    def scrape_twitter_200limit(t_api, q):

        query = 'from:' + q

        print "Query: " + query

        count = 200  # * 10 = the number of tweets to collect

        search_results = t_api.search.tweets(q=query, count=count, user='WAbbott')
        statuses = search_results['statuses']

        # iterate through 5 more batches of results by following the cursor
        tcount = 0
        for _ in range(5):
            print "Tweets collected so far: ", len(statuses)
            try:
                next_results = search_results['search_metadata']['next_results']
                tcount += 100
            except KeyError, e:  # no more results when next results doesnt exist
                break

            # create a dictionary from next_results, which has the following form:
            # ?max_id=313419052523346534&q=NCAA&include_entities=1
            kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

            search_results = t_api.search.tweets(**kwargs)
            statuses += search_results['statuses']

            # show one sample search result by slicing the list...
            # print json.dumps(statuses[0], indent=1)

        print "Total Number of Tweets Collected: " + str(len(statuses))
        return statuses

    @staticmethod
    def scrape_twitter_timeline(t_api, query):

        print "Collecting most recent tweet_Id for max_id pagination ..."
        user_timeline = t_api.statuses.user_timeline(screen_name=query, count=1)
        most_recent_tweet_id_arr = [user_timeline[0]['id']]
        # print "User Timeline ID : " + str(mostRecentTweetId)
        statuses = []

        for i in range(0, 10):  # iterate through all tweets (10 * 200 = 2000 tweets)
            # tweet extract method with the last list item as the max_id
            user_timeline = t_api.statuses.user_timeline(screen_name=query, count=200,
                                                         include_retweets=False,
                                                         max_id=most_recent_tweet_id_arr[-1])

            for tweet in user_timeline:
                # print tweet['text']  # print the tweet
                statuses.append(tweet)
                most_recent_tweet_id_arr.append(tweet['id'])  # append tweet id's
            print "Collected " + str(len(statuses)) + " tweets so far ..."

        print "Total Number of Tweets Collected: " + str(len(statuses))
        return statuses



