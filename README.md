# CodeFunDo
Repository for CodeFunDo++

### Managing Natural Disaster
The App will initially take the location of the user. Here user is the one willing to help in the rescue operation. The app is built only for that particular city where the disaster has occured. Based on the location given They get to choose the resuce volunteer group or if there isn't any create a new one. For this user must be registered.

For the data, Twitter is a gold mine of data. Unlike other social platforms, almost every user’s tweets are completely public and pullable. Most popular hashtags are used to get tweets using the twitter standard/premium API. With the tweets available I can group tweets based on time, day and location. Tweets will be updated every 15 minutes using since ID and maxid of the tweets. I run 2 files to get tweets one to get forward tweets ie from that particular timestamp and the other from that particular timestamp to the desired date specified(Date of the disaster-move back in time).

These tweets will be visulaized. Time based analysis will help to know at which time the help is needed the most. Location based visulaization to know which location is affected the most. The main page will display the corresponding graphs and will display the tweets with maximum no. of favorites, retweets. Since tweet results are in the form of json, I will explore all the other fields that tweet gives and do visulaization.

This visulization is location specific ie based on the location that user enters. This visulization will help the rescue volunteer/group to understand the situation faster and act on it. Natural disaster leads to loss of human life and some missing people. We will have the database of all the people of that area which the user selects. This list will be given to the rescue group. They will have a dashboard in which they can mark them safe or unsafe or dead.
