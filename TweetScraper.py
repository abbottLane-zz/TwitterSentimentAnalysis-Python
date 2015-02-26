import json
import twitter
import nltk

__author__ = 'wlane'


class TweetScraper:
    def __init__(self):
        pass

    # Returns a count of how many tweets were collected
    @staticmethod
    def scrape_twitter(t_api, q):

        query = 'from:' + q

        print "Query: " + query

        count = 300  # * 10 = the number of tweets to collect

        search_results = t_api.search.tweets(q=query, count=count, user='WAbbott')
        statuses = search_results['statuses']

        # iterate through 5 more batches of results by following the cursor
        count = 0
        for _ in range(5):
            print "Tweets collected so far: ", len(statuses)
            try:
                next_results = search_results['search_metadata']['next_results']
                count += 100
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






