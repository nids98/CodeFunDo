# CodeFunDo
Repository for CodeFunDo++

### Managing Natural Disaster
The App will initially take the location of the user. Based on the location given They get to choose the resuce volunteer group or if there isn't any create a new one.
For the data I will require data from social Media. Twitter is the great source of data. Most popular hashtags are used to get tweets using the twitter standard/premium API. With the tweets available I can group tweets based on time, day and location. Tweets will be updated every 15 minutes that is made sure by the since ID and maxid of the tweets. I run 2 files to get tweets one to get forward tweets from that particular timestamp and the other from that particular timestamp to the desired date specified(Date of the disaster).
The tweets are visulaized. Time based analysis will help to know at which time the help is needed the most.
