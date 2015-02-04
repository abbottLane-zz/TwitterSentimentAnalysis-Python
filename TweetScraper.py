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

        query = q

        count = 100

        search_results = t_api.search.tweets(q=query, count=count)
        statuses = search_results['statuses']

        # iterate through 5 more batches of results by following the cursor
        for _ in range(9):
            print "Tweets collected so far: ", len(statuses)
            try:
                next_results = search_results['search_metadata']['next_results']
            except KeyError, e:  # no more results when next results doesnt exist
                break

            # create a dictionary from next_results, which has the following form:
            # ?max_id=313419052523346534&q=NCAA&include_entities=1
            kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

            search_results = t_api.search.tweets(**kwargs)
            statuses += search_results['statuses']

            # show one sample search result by slicing the list...
            # print json.dumps(statuses[0], indent=1)

        # write all tweets to text file
        txtFile = open("tweets.txt", 'w')
        count = 0

        for tweet in statuses:
            count += 1
            txtFile.write(str(count) + ": " + tweet['text'].encode('utf-8')+"\n")

        print "Total Number of Tweets Collected: " + str(count) + "\n" + "Tweet text successfully saved to tweets.txt"
        return statuses






