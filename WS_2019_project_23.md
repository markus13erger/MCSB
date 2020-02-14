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
To create the ontology, we decided to use WebVOWL since it is more beginner friendly and basic than protégé. We followed steps of the "Ontology Creating 101" paper to create our ontology. This was originally written for protégé but can also be applied for other ontology editing services. The whole process of creating a fitting ontology was pretty iterative and we had to often revise it when working on the knowledge graph.

Seen below is the complete ontology in WebVOWL. We have a total of five classes (User, Artist, Word, Search and Song) with multiple properties:

![Ontology](https://raw.githubusercontent.com/markus13erger/MCSB/master/MCSBOntology.png)

## Task 4: Create a Knowledge Graph
Before creating a RDF file the data needed some pre-processing first using R. Then to lift the obtained data to RDF we tried using OpenRefine, but it was not very intuitive, so we decided to switch to Python for which the RDFlib package is available, which allowed us to transform our data into an RDF file with XML format. In the beginning we created three different RDF files for the lyrics, Google and Spotify data each, but then we realised that the relations between our classes are better shown in one single RDF file. Therefore, we combined all of the three existing RDF files into one.

### Markus Sieder
#### Spotify Data:
As already mentioned all of the data was pre-processed in R. We used the package "jsonlite" to read the "spotify_data.json" file. Afterwards I removed all rows which included songs that were played less than 10.000 ms (10 sec), because these were probably just skipped and not played, therefore they were not interesting for our application. I also removed spaces from the song and artist names and filled them with "+" instead, otherwise we encountered problems with the RDF creation.  Afterwards the data was saved as a CSV file.

In Python I realised that the songs from the artist "Vigiland" were not correctly saved in the CSV file, so I removed them. Afterwards I did reset the index such that there was a complete index from 1 to n. For the RDF file we defined the classes "Artist" and "Song". Where the "Artist" performs the "Song". The "Artist" has an "artistName" and the time one listened to this artist called "artistPlayed". The "Song" has a "songTitle" and also the time played "songPlayed".

#### Lyrics Data:
The lyrics data set did not need any additional pre-processing in R.

In Python I removed the line breaks, such that the words of the lyrics were just separated by a single space " ". Additionally, I removed the spaces in the artist and song name by "+", because otherwise this would later cause problems when lifting the data to RDF. Finally, I removed any stop words from the lyrics, because they would overshadow any useful words in their frequency. To create the RDF file, I used the class "Artist" once again which has an "artistName" and sings "Song". The "Song" contains the new class "Word" and has a "songTitle".

### Markus Berger
#### Google Data:
The file "google_data.json" was also pre-processed in R, where I removed unnecessary columns until there were just two columns for the words searched and the time searched left. The time stamp needed some transformation to be more readable. Additionally, there were some words added, especially "Nach" (German for "for") and "gesucht" (German for "searched") which were included in the beginning and ending of nearly every search. These needed to be removed. Non-ASCII characters would also lead to problems and where therefore also removed. Finally, the searches contained a lot of URLs which were also removed. To round things up the columns were renamed to "words" and "searchTime" and the index was reset. The pre-processed data was saved as a CSV file.

Next on I started working with Python to lift the data to RDF. There I had to add an extra column for the ID so we could later identify specific searches. I also removed the stop words just as we did with the lyrics. For the RDF transformation I created the class "Search" which has an exact time stamp "searchTime" and an individual "searchID". The class "Search" contains "Word" which consists of all the search words respectively.

#### User Data
We also created the class "User" where we did not have a data set. We just created ourselves since we listened to "Song" and wrote "Search". "User" also has an "userName" and an "userAge".

### Complete RDF
After creating all classes and their properties we combined them all into one RDF file which precisely reflects our ontology. This made it easier for the next step when loading our knowledge graph into a triple store.

## Task 5: Load your Knowledge Graph into a triple store
We used Graph DB as a triple store just as proposed. We had to adjust our RDF enrichment a few times to get everything right, but when we started to use a single RDF file everything worked just fine.

## Task 6: Develop a set of SPARQL queries to answer the competency questions

### 1. Who is the artist of a specific song? (Berger)

#### Query:
CONSTRUCT {<br/>
    ?artist foaf:sings ?song .<br/>
    ?song foaf:sungby ?artist .<br/>
} WHERE {<br/>
    ?artist foaf:sings ?song .<br/>
    ?song foaf:contains ?word .<br/>
    ?artist foaf:name ?aname .<br/>
    ?song foaf:title "Dancing+Queen" .<br/>
    ?word foaf:value ?cname .<br/>
}

#### Description:
This query returns the artist of a specific song (Dancing Queen in this case). It is also worth mentioning that there are song title which were used multiple times and are therefore performed by multiple artists.


### 2. Who is the most listened artist by a user? (Sieder)

#### Query:
SELECT DISTINCT ?time ?artist ?name<br/>
WHERE {<br/>
	?artist foaf:performs ?song .<br/>
   	 ?artist rdf:type ?Artist .<br/>
   	 ?song rdf:type ?Song .<br/>
   	 ?markus foaf:artist_listened ?artist.<br/>
    	 ?artist foaf:artist_ms ?time .<br/>
    	 ?song foaf:title ?title .<br/>
   	 ?artist foaf:name ?name .<br/>
} ORDER BY DESC(xsd:nonNegativeInteger(?time))<br/>

#### Description:
This query returns the milliseconds played of any artist and orders them by descending order. Therefore, the number one entry is the most listened artist of a user.


### 3. What are the lyrics of a specific song? (Berger)

#### Query:
CONSTRUCT {<br/>
    ?a foaf:contains ?b .<br/>
} WHERE {<br/>
    ?c foaf:sings ?a .<br/>
    ?a foaf:contains ?b .<br/>
    ?c rdf:type ?artist .<br/>
    ?a foaf:title "Dancing+Queen" .<br/>
    ?b rdf:type ?value .<br/>
    ?a rdf:type ?song .<br/>
}

#### Description:
This query returns all the words used in a specific song (in this case once again Dancing Queen).


### 4. What are the users searching for? (Sieder)

#### Query:
CONSTRUCT {<br/>
    ?u foaf:searched_word ?w .<br/>
} WHERE {<br/>
    ?se foaf:search_contains ?w .<br/>
    ?u foaf:searched ?se .<br/>
    ?u rdf:type ?User .<br/>
    ?w rdf:type ?Word .<br/>
}

#### Description:
This query returns all the words a user has searched for. In this case it just returns everything for the user Markus since this is the only user in our data.

### 5. Are the users searching for songs they listened to? (Berger)

#### Query:
SELECT DISTINCT ?s<br/>
WHERE { <br/>
    {<br/>
    ?u foaf:song_listened ?s .<br/>
    ?s rdf:type ?Song .<br/>
    ?u rdf:type ?User .<br/>
    ?w rdf:type ?Word .<br/>
    ?se rdf:type ?Search .<br/>
    ?se foaf:search_contains ?w .<br/>
    ?s foaf:title ?x .<br/>
    ?w foaf:value ?y .<br/>
        FILTER(?x=?y) .<br/>
   }<br/>        
} 

#### Description:
This Query looks up all unique songs that the user searched for. In total, there are only 13 songs that the user also searched for on google. In our case it is only possible to check one word as a time which results in troubles if the song title contains more than one word (for example "Dancing Queen"). This is a problem resulting from our song titles, since we chose to use song titles separated with a "+" (e.g. "Dancing+Queen"), where we could have introduced a new variable for title that links back to our rdf:Word. This is something we did not consider but is an important aspect for future projects.

### 6. Are the users searching for lyrics they listened to? (Sieder)

#### Query 1:
CONSTRUCT {<br/>
    ?u foaf:searched_word ?w .<br/>
    ?u foaf:song_listened ?s.<br/>
    ?s foaf:song_contains ?w .<br/>
} WHERE { <br/>
    {?se foaf:search_contains ?w .<br/>
    ?s foaf:song_contains ?w .<br/>
    ?u foaf:searched ?se .<br/>
    ?s rdf:type ?Song .<br/>
    ?u rdf:type ?User .<br/>
    ?w rdf:type ?Word .<br/>
    ?se foaf:id "824" .}<br/>
}

#### Query 2:
SELECT DISTINCT ?a <br/>
WHERE { <br/>
?u foaf:song_listened ?s .<br/>
    ?s foaf:song_contains ?a .<br/> 
    ?se foaf:search_contains ?b .<br/>
    ?a rdf:type ?Word .<br/>
    ?b rdf:type ?Word .<br/>
    ?s rdf:type ?Song .<br/>
    ?u rdf:type ?User .<br/>
    ?se rdf:type ?Search .<br/>
    ?a foaf:value ?x .<br/>
    ?b foaf:value ?y .<br/>
        FILTER(?x=?y) .<br/>
}

#### Description:
For the last competency question we wanted to answer, whether users are searching for lyrics they listened to. To answer this we selected two queries. Query one looks up all songs (their lyrics) that are connected to a single search. In our case we selected search number 824 containing the words "Go" and "Sky". It shows all songs that are have either words "Go" or "Sky" in their lyrics aswell as those, that contain both. <br/><br/>
The second Query is another approach where we look up which words that are contained in the lyrics have been searched by a user. 614 words from song lyrics have also been searched by the user. None of the queries puts an emphasis on the sentiment. We did not find a reasonable way to analyse whether the user actually searched for the lyrics to find a song or if the overlap as a mere coincidence. In general, all queries were processed very fast except the second query of this task, which took around 15 minutes.
