from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="m3USj4URYqfbkhOuiBaf2zzhY"
consumer_secret="qdlQ5LV0nAhVS09BH9lfV8PTUtaZm2zT4kAvoSfCa3U6jOTY2s"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="1201654596-OVxltygt0tv4vxWekr4RK7o0cJlNXkCtEBtN0i2"
access_token_secret="WYPNP46Z3mWTAZyfr7qZ1IlEApQKWbbTgYUb9UMKCX9hH"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        tweet_text = ""
        #some custom code to iterate through JSON and grab tweet text
        for x in range(0, len(data)):
            #find "text": substring
            look_for_text = ""
            for y in range(x, x + 7):
                if (y < len(data) - 1):
                    look_for_text += data[y]

            if (look_for_text == "\"text\":"):
                #print(look_for_text)
                tweet_text = data[x: x + 150]

        print("Tweet Text: \n" + tweet_text)


        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['trump'])