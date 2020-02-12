# Semantic Web Assignment
# Introduction to Semantic Systems 2019W

## Task 1: Suggest a Semantic Application
### Description:
The suggested application is a service build on top of a knowledge graph, which allows the users to explore and analyse their music consumption and their search behaviour. The focus lies especially on the connections of these two. Spotify data will be used for the music consumption and Google data will be used for the search behaviours of the users. These two different data sets will be connected by a lyrics dataset which enables the users to compare the lyrics of the songs they heard with their personal Google searches.

### This results in the following competency questions:
- Who is the artist of a specific song?
- What are the lyrics of a specific song?
- What are the users searching for?
- Are the users searching for artists they listened to?
- Are the users searching for songs they listened to?
- Are the users searching for lyrics the listened to?

### Images and UI mock-up of the semantic application idea:
-- Missing --
 
## Task 2: Data Collection
Since we were only left with two group members, one of us was responsible for collecting two different datasets, such that we have all the data to build our semantic app.
### Markus Berger:
#### Spotify Data:
After a quick google search I found a link to request my personal data according to the GDPR regulations, which is explicitly stated on their homepage. How to get the personal data is not directly stated, but when logging in on their homepage and going to the privacy settings I found a step by step guide to get my data.
- Step 1 was to simply request the data from Spotify such that they will start compiling my personal data.
- Step 2 is to wait for the compiling to finish which can take up to 30 days (for me it took 14 days on my first request and 12 days on my second request when I wanted updated data for this project).
- Step 3 is enabled when the data is ready to download. I received an email and simply had to click their download link.
During the whole process I could not decide which data I wanted, but apparently, they just give you everything they have. This also includes subscriptions, playlists, interactions with other users and most importantly a list of all the music tracks I listened to. All the data was stored in different JSON files.

Since only the music track list is relevant for us, I will just describe this data. There was a total of 2021 songs listed (according to the Spotify homepage this includes just the songs I listened to in the last 90 days, because they delete this personal data afterwards). The songs have a “endTime” variable (the date and time when I stopped playing them, exact to the minute), an “artistName”, a “trackName” of course and “msPLayed” (the time I played this song in milliseconds).
The data was very clean and did not need that much processing, but I removed all song with less than 10.000 milliseconds (10 seconds) played, because this were just songs that I skipped over and did not listen to. There are also hardly any words spoken in the first ten seconds which could influence my Google searches. This reduced the total amounts of songs to 1.556.

#### Lyrics Data:
To connect the song lyrics to our Google searches we needed a data set which has as many lyrics as possible. After some research I found a dataset on Kaggle which included more than 55.000 songs with their respective lyrics. Since this does not include any personal data it was much easier to obtain this dataset. I could simply download the data which was stored as an CSV file and inspect it.

The exact number of songs is 57.650 and the dataset contains the name of the artist, the song names, a link to a webpage to listen to the song (YouTube, Vimeo, etc.) and unmodified lyrics of the song. The dataset was originally created by scraping the content from a webpage called “Lyrics-Freak”, Thankfully this was already done for our convenience which saved a lot of time.
While processing extremely short and extremely long lyrics were removed as well as lyrics with non-ASCII symbols.

### Markus Sieder:
#### Google Data:
To get my personal Google data I used the Google Takeout service which is provided when logging into my Google account. This service allows to download all kinds of data which Google saves, from YouTube searches to Google fit data there was a total of 46 different categories. It is not explicitly stated where my Google searches are saved, so I downloaded a bunch of different options which could include my search history. After selecting the datasets, I got a notification that it can take from some minutes up to several days until Google has compiled all my data, depending what datasets I requested and how big they are.

Thankfully after just an hour I got an email notifying me that my data is ready for download. After looking through all the data with a lot of different formats I finally found my search history in the “my activities” dataset. Unfortunately, the data was saved in a HTML file which was not very useful. Back to the Google takeout service I found that for some datasets different data formats can be selected, therefore I chose a JSON format for my search history. Since I already knew what to request it just took some minutes to compile my data.

Finally, I got the needed dataset which included the searched terms, an URL for the Google search and a timestamp, exact to the millisecond. Since the search variable was always constructed like “Nach” + “actual Google search” + “gesucht” (“Nach gesucht” is “searched for” in German) this data needed some processing first. Therefore, it was loaded into RStudio and the searches were cleaned.

## Task 3: Create an ontology that models the selected domain
To create the ontology we decided to use WebVOWL since it is more begginer friendly and basic than protégé. We followed steps of the "Ontology Creating 101" paper to create our ontology. This was originally written for protégé but can also be applied for other ontology editing services.

Seen below is the complete ontology in WebVOWL. We have a total of five classes (User, Artist, Word, Search and Song) with multiple properties:

