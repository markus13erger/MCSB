# MCSB Application and GraphDB
## Music Choices and Search Behavior Application and GraphDB

### A guide how to use the application or GraphDB

1. Get the datasets needed:
  - spotify data: Go to https://www.spotify.com/at/account/privacy/ and follow the steps in "Download your data". When you receive the data look for the "StreamingHistory0.json" file and save it in the "data" folder. Also rename it to "spotify_data".
  - google data: Go to https://takeout.google.com/settings/takeout?pli=1 and choose to request "My activities" as a JSON file. Follow the steps until you receive the data, save it in the "data" folder and rename it to "google_data".
  - lyrics data: Go to https://www.kaggle.com/mousehead/songlyrics/data and click the download link. Save it in the "data" folder and rename it to "lyrics_data".

2. Pre-process the data sets:
  - Run the "pre-processing" jupyter notebook to pre-process the data. Afterwards all the available files should be saved as CSV files in the "data" folder.

3. Enrich data to RDF:
  - Run the "transformation" jupyter notebook to enrich the datasets to RDF files. After running the notebook all the datasets should be combined to one RDF file in the "data" folder called "MCSB".

4a. Run the application "application.py" with the following arguments: 
  - file (the filepath of the "MCSB" RDF file)
  - query (which query you want to use, either "song" or "time")
  - artist (for which artist you want to query)
 
 With the "-h" argument there are more details shown concerning the mandatory arguments.
 
4b. Download GraphDB Free on https://www.ontotext.com/products/graphdb/graphdb-free/ and follow the installation steps until finished. When everything is finished the the "MCSB" RDF file can accessed and queried with GraphDB.
