#building a query - tweets with the #bridgerton that are not retweets
query = '#EXPO_2030,#EXPO2030 -filter:retweets'
# we obtain a maximum of 1000 tweets
max_tweets = 1000

# we store the tweepy.Cursor response of each tweet in a list
search_tweets = [tweet for tweet in tweepy.Cursor(api.search_tweets,
                                                  q=query,
                                                  lang='en',
                                                  tweet_mode='extended').items(max_tweets)]

# we store the text of each tweet in a list
tweets_text = [tweet.full_text for tweet in search_tweets]
print(tweets_text)