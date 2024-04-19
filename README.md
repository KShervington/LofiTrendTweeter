# LofiTrendTweeter

- `trendGetter.py` is the primary file which makes the requests to the Twitter API, parses the responses, updates local JSON files, and decides the content of the final tweet.
- `sky_generator.js` interacts with an open photoshop instance to modify several values of the active layer to create a specified amount of unique pictures.
- `application.py` is what allows the program to run in the AWS Elastic Beanstalk environment.

There are a few other supporting files that I did not include due to lack of relevancy.

### References
[How to Make a Twitter Bot in Python using Tweepy](https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/)<br />
[Automate Getting Twitter Data in Python Using Tweepy and API Access](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/)<br />
[Twitter API](https://developer.twitter.com/en/docs/twitter-api/v1/trends/trends-for-location/api-reference/get-trends-place)<br />
[Photoshop Scripting API](https://theiviaxx.github.io/photoshop-docs/Photoshop/ArtLayer.html)
