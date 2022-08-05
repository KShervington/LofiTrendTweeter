import os
import requests
import json
import random
import tweepy as tw
import pandas as pd

consumer_key= '###############################'
consumer_secret= '###############################'
access_token= '###############################'
access_token_secret= '###############################'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("AUTHENTICATION SUCCESSFUL")
except Exception as e:
    print("AUTHENTICATION ERROR:")
    print(e)
    exit()

print()

try:
    # get json of the top 10 trending terms in the US
    x = api.get_place_trends(id=23424977)

    # Randomly choose one of the search terms
    spot = random.randint(0,10)

    currTopic = x[0]['trends'][spot]['name'] # Get today's topic
    print("Current topic is " + currTopic)
    print()

    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + "/TweetData.json"
except Exception as e:
    print("ERROR:")
    print(e)
    exit()

# Do this like following file manipulations to allow file editing
with open(file_path, "r+") as td_file:
    #td_file = open("C:/Users/kyles/OneDrive/Desktop/TrendTweeter Resources/TweetData.json")
    data = json.load(td_file)
    print("Printing full json...")
    print(data)
    print()
    print("Printing just \"Previous Topic\"...")
    print(data['Trend Topic'])
    print()
    print("Printing just \"Picture Number\"...")
    print(data['Picture Number'])
    print()
    print("Changing \"Picture Number\" to 52 and printing...")
    data["Picture Number"] = data['Picture Number'] + 1

    td_file.seek(0)
    json.dump(data, td_file)
    td_file.truncate()

    print(data['Picture Number'])
    print()

    td_file.close()


with open(file_path, "r") as p: 
    data = json.load(p)
    prevTopic = data["Trend Topic"] # Read topic already in the file

    print("Previous topic is " + prevTopic)

    # If current topic is duplicate or similar, find a different one
    if prevTopic != None and prevTopic in currTopic or currTopic in prevTopic:
        print("Found similar topic!")

        # Iterate through first 10 topics to find a different one
        for i in range(11):
            currTopic = x[0]['trends'][i]['name']

            # Break when today's topic is different from previous
            if currTopic != prevTopic:
                print("New current topic is " + currTopic)
                break

    p.close()


# Write the day's topic to the respective file
with open(file_path, "r+") as o:
    data = json.load(o)

    print("Writing " + currTopic + " to file!")
    print()

    # Write current topic to file
    data["Trend Topic"] = currTopic

    o.seek(0)
    json.dump(data, o)
    o.truncate()
    
    o.close()


with open(file_path, "r") as h:
    data = json.load(h)

    try:
        image_path = absolute_path + "/lofi sky(dump)/" + str(data["Picture Number"]) + ".jpg"
        media = api.media_upload(image_path)
    except Exception as e:
        print("FAILED uploading image due to ERROR:")
        print(e)

        h.close()
        exit()

    try:
        print("Sneding tweet...")

        api.update_status(data["Trend Topic"], media_ids=[media.media_id])

        print("Tweet sent!!!")
    except Exception as e:
        print("FAILED sending tweet due to ERROR:")
        print(e)

    h.close()

exit()

# Send out a tweet
#api.update_status("this is a test tweet. Today's topic is: " + currTopic)

#newTweet = api.update_status("this is a test tweet. Today's topic is: " + currTopic)
#print("Sent the following tweet:\n" + newTweet)