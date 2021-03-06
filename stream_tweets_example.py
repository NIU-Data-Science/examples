import tweepy

#override tweepy.StreamListener to add logic to on_status

#This particluar class will print the tweet status.  Note that you can change "print()" to other functions.
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

#Instantiate API authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

#Instantiate stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#In this example we will use filter to stream all tweets containing the word python. The track parameter is an array of search terms to stream.

myStream.filter(track=['python'])

#This example shows how to use filter to stream tweets by a specific user. The follow parameter is an array of IDs.

myStream.filter(follow=["2211149702"])

#This example will limit our tweets to tweets that originate from Moscow.
myStream.filter(locations=["37.3193,55.5539,37.9401,55.9388"])
