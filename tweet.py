import os # To access our OS environment variables
import markov
import twitter

#Using Python os.environ to get at environmental variables
#
#Note: you must run 'source.secrets.sh' before running this file
#to make sure these environmental variables are set

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

#This will print info about credentials to make sure they are correct. 
print api.VerifyCredentials()



generator = markov.MarkovMachine()
generator.read_files(["frost.txt", "places.txt"])
randtxt = generator.make_text()
status = api.PostUpdate(randtxt)
print status.txt

