# MCSB
## Music Choices and Search Behavior

1. Get the datasets needed:
  - spotify data: Go to https://www.spotify.com/at/account/privacy/ and follow the steps in "Download your data". When you receive the data look for the "StreamingHistory0.json" file and save it in the "data" folder. Also rename it to "spotify_data".
  - google data: Go to https://takeout.google.com/settings/takeout?pli=1 and choose to request "My activities" as a JSON file. Follow the steps until you receive the data, save it in the "data" folder and rename it to "google_data".
  - lyrics data: Go to https://www.kaggle.com/mousehead/songlyrics/data and click the download link. Save it in the "data" folder and rename it to "lyrics_data".

2. Pre-processing
  Run the "pre-processing" jupyter notebook to pre process the data. Afterwards all the available files should be saved as CSV files in the "data" folder.
