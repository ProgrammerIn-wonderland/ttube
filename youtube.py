#!/usr/bin/env python3
from youtube_search import YoutubeSearch
import os

results = YoutubeSearch(input("video search: "), max_results=10).to_dict() # search videos

mapper = {} # init map

i = 0
for result in results: # for each result...
    mapper[i] = result["id"] # set the map to have the ID
    print(str(i) + ": " +result["title"]) # output the map ID and the video totle
    i=i+1 # increment 

choice = mapper[int(input("which choice? "))] # get ID of choice
url = "https://www.youtube.com/watch?v=" + choice # full youtube url from ID

os.system(" mplayer -ao pulse -vo fbdev2 -cache 131072 -fs -zoom -xy 1080 $(yt-dlp -q -f 18 \"" + url + "\" -g)") # change 1080 to your screens first resolution number
